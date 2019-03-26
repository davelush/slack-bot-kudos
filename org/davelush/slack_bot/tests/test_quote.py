from org.davelush.slack_bot.quotegenerator import QuoteGenerator


class TestQuote(object):

    def test_quote_not_none(self):
        quoteGen = QuoteGenerator()
        for x in range(100):
            quote = quoteGen.random()
            print(quote)
            assert quote is not None
