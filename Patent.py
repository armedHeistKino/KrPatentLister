# 발명인, 출원인, 대리인의 정보를 저장하는 클래스
class Juridical:
    def __init__(self):
        self.name = None            # 성명
        self.englishName = None     # 영문성명
        self.country = None         # 국가
        self.address = None         # 주소
        self.code = None            # 구분코드

    def setJuridical(self, name, englishName, country, address, code):
        self.name = name
        self.englishName = name
        self.country = country
        self.address = address
        self.code = code

# 특허 문서의 사항을 저장하는 클래스
class PatentForm:
    def __init__(self):
        self.treeReference = None

        # 문서 사항
        self.abstract = None                    # 초록
        self.claim = None                       # 청구항
        
        # 발명인
        self.inventor = list()
        
        # 출원인
        self.applicant = Juridical()

        # 대리인
        self.agent = Juridical()

        # 국제 출원
        self.patentCooperationOpenDate = None           # 공개날짜
        self.patentCooperationOpenCode = None           # 공개구분코드
        self.patentCooperationApplicationDate = None    # 출원날짜
        self.patentCooperationApplicatoinCode = None    # 출원구분코드

        # 우선권주장
        self.priorityClaimCountry = None               # 주장국가
        self.priorityClaimDate = None                  # 주장날짜
        self.priorityClaimCode = None                  # 주장구분코드 

    def print(self):
        for inventor in self.inventor:
            print("발명인 ", self.inventor.name, "(",self.inventor.englishName, ")")
        print("출원인 ", self.applicant.name, "(",self.applicant.englishName, ")")
        print("대리인 ", self.agant.name, "(",self.agent.englishName, ")")
        
        print("요약")
        print(self.abstract)
        print("청구항")
        print(self.claim)