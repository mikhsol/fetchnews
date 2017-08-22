import unittest

from bs4 import BeautifulSoup

AUTHORS = ["Calla Wahlquist", "Gareth Hutchens"]
HEADLINE = "Coalition says citizenship crisis will last months but MPs " \
           "will keep voting"
DATE = "Sunday 20 August 2017 05.34 BST"
TEXT = "The Turnbull government says if any more Coalition MPs are found to be dual citizens they will continue to " \
       "vote in parliament until the high court settles their eligibility.Arthur Sinodinos, the minister for " \
       "industry, innovation and science, has said it was wrong for theNationals senator Matt Canavan to promise to " \
       "refrain from voting in parliamentafter he discovered he held dual Italian citizenship, because he did so when " \
       "he did not know all the details of his case.He said the Nationals leader, Barnaby Joyce, and the deputy " \
       "Nationals leader, Fiona Nash –who have also discovered they are dual citizens– were right to keep voting in " \
       "parliament until their eligibility was settled by the high court.He said Joyce and Nash would be the standard " \
       "for any other Turnbull government MPs who may be found to be dual citizens.“I think the standard that’s been " \
       "set will now stick,” Sinodinos told the ABC on Sunday. “What we need to do is make sure everybody takes " \
       "responsibility for their own situation, in terms of members of parliament, and we work our way through this " \
       "as quickly as possible, get the high court to make decisions relevant to what’s going on and we move on.”The " \
       "decision to keep all Coalition MPs voting in parliament is an attempt by the Turnbull government to retain " \
       "control of the House of Representatives, where it holds a one-seat majority.The attorney general, " \
       "George Brandis, believes the high court won’t be dealing withthe citizenship crisis that has embroiled seven " \
       "MPs and senatorsuntil October, leaving that majority in the balance.If Joyce is found by the court to be " \
       "ineligible to sit in the parliament, it would trigger a byelection in his seat of New England.Brandis said " \
       "the legal advice he had received said there was no problem with Joyce and Nash remaining in the cabinet and " \
       "making executive decisions.“If there is anyone who is a threat to the integrity of the parliament at the " \
       "moment is [opposition leader Bill] Shorten because of the devious tactics he has employed,” he said.Shorten, " \
       "whose father was born in the UK, said on Sunday that he renounced his British citizenship “many years ago” " \
       "but would not provide documentary evidence, telling reporters: “I don’t feel any obligation to justify what I " \
       "have just said because I know it to be true ... I don’t expect every MP to have to jump through hoops to " \
       "start meeting a standard that we have already met.”Shorten said all candidates for federal parliament should " \
       "be aware of the citizenship requirements and criticised the government for turning a legal issue into a " \
       "“parliamentary farce”.“The advice about section 44 is on the candidates’ form when people nominate so it’s a " \
       "matter of just reading the fine print,” he said. “Perhaps this is a problem in terms of the constitution that " \
       "has been ignored but it is still the constitution of Australia and, until the constitution is changed, " \
       "it’s the law.”Shorten did, however, say he was willing to offer the federal government a “peace treaty” over " \
       "the citizenship crisis. The Labor leader said Joyce and Nash should stand aside until the high court decides " \
       "their fate but was willing to discuss the matter with the prime minister. However, he suggested that, " \
       "if there was a controversial vote to be had in parliament, it should wait until the high court has made its " \
       "decision.“I think Australians want to see this government focusing on them, not these legal and political " \
       "games,” Shorten said.Sinodinos dismissed concerns that the validity of Turnbull government decisions could be " \
       "challenged in court if Coalition MPs were proven to have been ineligible.“The advice I have received to date " \
       "is that decisions in the parliament and decisions by ministers, the validity of those decisions, will not be " \
       "affected,” he said.ABC host Chris Ulhmann then asked: “If it turns out that Barnaby Joyce should not have " \
       "been in cabinet … people can take it to court, and we’ve seen plenty of ‘lawfare’, particularly from " \
       "environmental groups, they may well decide to test that argument in another court?”Sinodinos replied: “I’m " \
       "not going to speculate on where the high court will come out. The point is that there was very strong advice " \
       "given to the government about whether Mr Joyce stands [and] Fiona Nash.”On Saturday, the crossbench " \
       "senatorNick Xenophonsaid he would become the seventh MP to refer himself to the high court after he " \
       "discovered he was a British overseas citizen.He said he had received advice from the British Home Office that " \
       "it considered him a British overseas citizenbecause his father, Theodoros Xenophou , was from Cyprus – a " \
       "British colony until 1960 – and moved to Australia in 1951.When Cyprus gained independence, most Cypriots " \
       "lost their British citizenship except those who moved to one of nine countries, including Australia. This " \
       "made Xenophon’s father a British overseas citizen, a status that automatically extended to Xenophon, " \
       "who was born in Australia.“The legal advice I have had is that I should just keep calm and carry on and wait " \
       "for the high court to determine this,” he told the Nine network on Sunday.On Sunday Shorten denied " \
       "allegations Labor staffers had been involved in uncovering details of Xenophon’s UK citizenship.“I rang " \
       "senator Xenophon last night,” he said. “I understand that he’s upset at what would seem to be clearly quite " \
       "an anachronism, a colonial loophole that he’s caught in... But I made it clear to him that whilst he may have " \
       "made some intemperate remarks, and I understand he would be upset about being in this predicament, " \
       "Labor had nothing to do with it. Full stop.”The parliament has already referred Canavan, the Greens senators " \
       "Larissa Waters and Scott Ludlam, and the One Nation senator Malcolm Roberts,as well as Joyce, to the court. " \
       "On Friday night, Nash revealed she was a UK citizen by descent – the third member of the prime minister’s " \
       "cabinet to be affected.The senior Nationals MP Darren Chester conceded it had been a “rotten few weeks” for " \
       "his party. “We need to be better at our vetting process when people nominate to be a candidate,” he told ABC " \
       "television.The high court will have a directions hearing on the matter on Thursday where a judge will get the " \
       "parties together and agree to a timetable over the various steps towards the hearings.“The commonwealth will " \
       "be asking the court to deal with the matter urgently,” Brandis told Sky News. While the court will have a " \
       "sitting in September, he thinks realistically the issue won’t be heard until the first fortnight of " \
       "October.The shadow attorney general, Mark Dreyfus, said the high court had a record of dealing very quickly " \
       "with urgent cases and hoped it will be cleared up within a couple of months.“I think every Australian will be " \
       "looking at this and thinking what a circus,” he told ABC television.Xenophon said Joyce’s decision not to " \
       "stand down was causing disruption on the floor of the House of Representatives.“It would probably be simpler " \
       "for the government if the ministers stood aside but it’s really a political issue, not a legal issue," \
       "” he later told Sky News.At the conclusion of the last federal election, the government entered agreements " \
       "for confidence and supply with some of the lower house crossbenchers as a precautionary measure, " \
       "but last week independent MP Bob Katter said he would no longer guarantee supply and confidence to the " \
       "government.Xenophon confirmed his NXT party would still support the government on matters of confidence and " \
       "supply.Australian Associated Press contributed to this report ".strip()


class HtmlProcessor(object):
    def __init__(self, html=None):
        self.soup = BeautifulSoup(html, "html.parser")

    def get_authors(self):
        authors = []
        for a in self.soup.find_all("a", {"rel": "author"}):
            authors.append(a.span.text)

        return authors

    def get_headline(self):
        return self.soup.find("h1", {"class": "content__headline"})\
            .text.strip()

    def get_date(self):
        d = self.soup.find("time", {"itemprop": "datePublished"})
        return d.text.strip().replace(u"\xa0", u" ")

    def get_text(self):
        t = self.soup.find("div", {"itemprop": "articleBody"})
        [div.extract() for div in t.findAll("div")]
        [aside.extract() for aside in t.findAll("aside")]
        return t.get_text(strip=True)


class TestHtmlProcessor(unittest.TestCase):
    def setUp(self):
        with open("test/data/raw_html.txt", "r") as f:
            raw_html = f.read()
        self.p = HtmlProcessor(raw_html)
        self.authors = self.p.get_authors()

    def test_get_author_details(self):
        self.assertTrue(self.authors[0] in AUTHORS)

    def test_get_few_authors_details(self):
        for a in self.authors:
            self.assertTrue(a in AUTHORS)

    def test_get_headline(self):
        self.assertEqual(self.p.get_headline(), HEADLINE)

    def test_get_date(self):
        self.assertEqual(self.p.get_date(), DATE)

    def test_get_text(self):
        self.assertEqual(self.p.get_text(), TEXT)
