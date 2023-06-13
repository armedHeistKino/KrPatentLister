import xml.etree.ElementTree as ET
import datetime as DT

import Patent

prefixNamespace = {
    'soapenv'   : 'http://schemas.xmlsoap.org/soap/envelope/',
    'ns'        : 'http://plus.kipris.or.kr/xsd',
    'ax2102'    : 'http://patentbean.services.webservice.plus.kipris.or.kr/xsd',
    'ax2104'    : 'http://comm.webservice.plus.kipris.or.kr/xsd'
}

class XmlParser:
    def parseToPatentForm(xml_root):
            newForm = Patent.PatentForm()

            # 문서 사항
            newForm.abstract = xml_root.find('.//ax2102:absractInfo/ax2102:astrtCont', prefixNamespace)
            newForm.claim = xml_root.find('.//ax2102:claimInfo/ax2102:claim', prefixNamespace)

            # 발명인
            # 발명인이 여러명일 수 있음.
            xmlInventors = xml_root.findall('.//ax2102:inventorInfo', prefixNamespace)
            for inventor in xmlInventors:
                newInventor = Patent.Juridical()
                newForm.append(newInventor.setJuridical(
                    inventor.find('.//ax2102:name', prefixNamespace),
                    inventor.find('.//ax2102:engName', prefixNamespace),
                    inventor.find('.//ax2102:country', prefixNamespace),
                    inventor.find('.//ax2102:address', prefixNamespace),
                    inventor.find('.//ax2102:code', prefixNamespace))
                )

            # 출원인
            newForm.applicant = Patent.Juridical(
                    xml_root.find('.//ax2102:applicantInfo/ax2102:name', prefixNamespace),
                    xml_root.find('.//ax2102:applicantInfo/ax2102:engName', prefixNamespace),
                    xml_root.find('.//ax2102:applicantInfo/ax2102:country', prefixNamespace),
                    xml_root.find('.//ax2102:applicantInfo/ax2102:address', prefixNamespace),
                    xml_root.find('.//ax2102:applicantInfo/ax2102:code', prefixNamespace)
            )

            # 대리인
            newForm.agent = Patent.Juridical(
                    xml_root.find('.//ax2102:agentInfo/ax2102:name', prefixNamespace),
                    xml_root.find('.//ax2102:agentInfo/ax2102:engName', prefixNamespace),
                    xml_root.find('.//ax2102:agentInfo/ax2102:country', prefixNamespace),
                    xml_root.find('.//ax2102:agentInfo/ax2102:address', prefixNamespace),
                    xml_root.find('.//ax2102:agentInfo/ax2102:code', prefixNamespace)
            )

            # 국제출원
            newForm.patentCooperationOpenDate = xml_root.find('.//ax2102:internationalInfo/ax2102:internationOpenDate', prefixNamespace)
            newForm.patentCooperationOpenCode = xml_root.find('.//ax2102:internationalInfo/ax2102:internationOpenCode', prefixNamespace)
            newForm.patentCooperationApplicationDate = xml_root.find('.//ax2102:internationalInfo/ax2102:internationalApplicationDate', prefixNamespace)
            newForm.patentCooperationApplicationCode = xml_root.find('.//ax2102:internationalInfo/ax2102:internationalApplicationNumber', prefixNamespace)


            # 우선권주장
            newForm.priorityClaimCountry = xml_root.find('.//ax2102:priorityInfo/ax2102:priorityApplicationCountry', prefixNamespace)
            newForm.priorityClaimDate = xml_root.find('.//ax2102:priorityInfo/ax2102:priorityApplicationDate', prefixNamespace)
            newForm.priorityClaimCode = xml_root.find('.//ax2102:priorityInfo/ax2102:priorityApplicationCode', prefixNamespace)


