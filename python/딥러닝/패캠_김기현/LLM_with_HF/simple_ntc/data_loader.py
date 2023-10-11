import torchtext
version = list(map(int, torchtext.__version__.split('.')))

# 현재 버전에 맞게 모듈을 가져오는 코드
if version[0] <= 0 and version[1] < 9:
    from torchtext import data
else:
    from torchtext.legacy import datasets

class DataLoader(object):
    """
    Data loader class to load text file using torchtext library.
    torchtext library를 사용해서 text 파일을 가져오는 DataLoad 클래스.
    """

    def __init__(
            self, train_fn,
            batch_size=64,
            valid_ratio=.2,
            device=-1,
            max_vocab=999999,
            min_freq=1,
            use_eos=False,
            shuffle=True
    ):
        '''
        DataLoader initialization
        :param train_fn : Train-set filename
        :param batch_size: Batchify data for certain batch size. # 특정 batch size로 데이터를 batch화함.
        :param device: Device-id to load data(-1 for CPU) # 데이터를 적재할 Device-id (-1은 CPU)
        :param max_vocab: Maximum vocabulary size
        :param min_freq: Minimum frequency for loaded word.
        :param use_eos: If it is True, put <EOS> after every end of sentence. # 만약 True면 모든 문장의 마지막에 <EOS> 토큰을 넣는다.
        :param shuffle: If it is True, random shuffle the input data.
        '''

        super().__init__()

        # Define field of the input file. # input file의 필드를 정의
        # The input file consists of two fields. # 입력파일은 두개의 필드로 구성됨
        self.label = data.Field(
            sequential=False,
            use_vocab=True,
            unk_token=None,
        )

        self.text = data.Field(
            use_vocab=True,
            batch_first=True,
            include_lengths=False,
            eos_token='<EOS>' if use_eos else None,
        )
        self.text = data.Field(
            use_vocab=True,
            batch_first=True,
            include_lengths=False,
            eos_token='<EOS>' if use_eos else None,
        )

        # Those defined two columns will be delimited by TAB. # 정의된 두 칼럼은 탭으로 구별됨.
        # Thus, we use TabularDataset to load two columns in the input file. # 따라서 우리는 입력 파일에 있는 두 칼럼을 TabularDataset를 사용해 가져옴.
        # We would have two separate input file: train_fn, valid_fn # 입력 파일을 train_fn과 valid_fn으로 구별해야함.
        # Files consist of two columns: label field and text field. # 파일들은 두개의 columns으로 구성됨 (label 필드와 text 필드)
        train, valid = data.TabularDataset(
            path=train_fn,
            format='tsv',
            fields=[
                ('label', self.label),
                ('text', self.text),
            ],
        ).split(split_ratio=(1-valid_ratio))


        # Those loaded dataset would be feeded into each iterator: # 불러온 데이터셋은 각 iterator로 들어감
        # train iterator and valid iterator. #
        # We sort input sentences by length, to group similar lengths. # 문장의 길이로 정렬하고 유사한 길이끼리 그룹핑한다.

        self.train_loader, self.valid_loader = data.BucketIterator.splits(
            (train, valid),
            batch_size=batch_size,
            device='cuda:%d' % device if device >= 0 else 'cpu',
            shuffle=shuffle,
            sort_key=lambda x: len(x.text),
            sort_within_batch=True,
        )

        # At last, we make a vocabulary for label and text field. # 마지막에 lable과 text field에 대한 vocabulary를 만든다.
        # It is making mapping tabel between words and indice. # 이건 단어와 indice 사이를 매핑하는 테이블을 만드는 것이다.
        self.label.build_vocab(train)
        self.text.build_vocab(train, max_size=max_vocab, min_freq=min_freq)