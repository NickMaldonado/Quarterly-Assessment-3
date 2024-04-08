import sqlite3

def insert_questions(questions, category):
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()

    for question_data in questions:
        question, option_a, option_b, option_c, option_d, answer = question_data
        cursor.execute('''INSERT INTO QuizQuestions (category, question, option_a, option_b, option_c, option_d, answer)
                          VALUES (?, ?, ?, ?, ?, ?, ?)''', (category, question, option_a, option_b, option_c, option_d, answer))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    business_strategy = [
        ('What business strategy framework was introduced by Michael Porter in 1979?', 'A) SWOT', 'B) Porter', 'C) Ansoff', 'D) BCG', 'B'),
        ('What is the term for the strategy involving the development and introduction of new products or services into existing markets?', 'A) Diversification', 'B) Market penetration', 'C) Market development', 'D) Product development', 'A'),
        ('In business strategy, what does the "S" in SWOT stand for?', 'A) Strategy', 'B) Strength', 'C) Scope', 'D) Situation', 'B'),
        ('What strategy involves a company lowering its prices to gain market share rapidly?', 'A) Differentiation', 'B) Cost Leadership', 'C) Penetration', 'D) Niche', 'C'),
        ('Which strategic planning tool visualizes the competitive positions of companies in an industry?', 'A) BCG Matrix', 'B) Ansoff Matrix', 'C) Porter\'s Five Forces', 'D) Boston Matrix', 'D'),
        ('What is the strategy where a company focuses on serving a specific segment of the market?', 'A) Cost Leadership', 'B) Differentiation', 'C) Focus', 'D) Diversification', 'C'),
        ('Which strategy focuses on reducing costs through efficient production and distribution processes?', 'A) Cost Leadership', 'B) Differentiation', 'C) Focus', 'D) Diversification', 'A'),
        ('What is the term for a strategic alliance between two or more companies to achieve a common objective?', 'A) Joint venture', 'B) Merger', 'C) Acquisition', 'D) Partnership', 'D'),
        ('What is the strategic approach that aims to create a unique and valuable position in the market?', 'A) Cost Leadership', 'B) Differentiation', 'C) Focus', 'D) Niche', 'B'),
        ('What strategy involves a company expanding its operations into new markets or industries?', 'A) Penetration', 'B) Expansion', 'C) Diversification', 'D) Integration', 'B')
    ]

    entrepreneurship = [
        ('Who is often regarded as the "father of modern entrepreneurship"?', 'A) Peter Drucker', 'B) Joseph Schumpeter', 'C) Adam Smith', 'D) Milton Friedman', 'B'),
        ('What term describes a business model that seeks to address a social or environmental issue while generating profit?', 'A) Social enterprise', 'B) Social innovation', 'C) Social entrepreneurship', 'D) Sustainable business', 'C'),
        ('Which Silicon Valley entrepreneur co-founded PayPal and later became the CEO of Tesla and SpaceX?', 'A) Jeff Bezos', 'B) Steve Jobs', 'C) Elon Musk', 'D) Mark Zuckerberg', 'C'),
        ('What is the term for a small amount of money invested in a startup in exchange for ownership equity?', 'A) Seed funding', 'B) Angel investment', 'C) Venture capital', 'D) Crowd funding', 'A'),
        ('What is the name of the phenomenon where entrepreneurs take failed ideas or businesses and turn them into successful ventures?', 'A) Pivot', 'B) Iteration', 'C) Revolution', 'D) Innovation', 'A'),
        ('What term describes the practice of bringing together resources to start a business venture?', 'A) Collaboration', 'B) Aggregation', 'C) Bootstrapping', 'D) Syndication', 'C'),
        ('Which entrepreneur famously dropped out of college to co-found Microsoft?', 'A) Steve Jobs', 'B) Bill Gates', 'C) Mark Zuckerberg', 'D) Larry Page', 'B'),
        ('What is the term for the process of strategically choosing which markets to enter with a new product or service?', 'A) Market development', 'B) Market positioning', 'C) Market segmentation', 'D) Market selection', 'D'),
        ('What is the name of the entrepreneur who co-founded Airbnb?', 'A) Brian Chesky', 'B) Travis Kalanick', 'C) Jack Dorsey', 'D) Evan Spiegel', 'A'),
        ('What term describes the strategy of rapidly scaling a business by reinvesting profits rather than seeking external funding?', 'A) Bootstrap financing', 'B) Organic growth', 'C) Angel investment', 'D) Venture capital', 'B')
    ]

    business_ethics = [
        ('What term refers to the ethical principle of being honest and truthful in business dealings?', 'A) Integrity', 'B) Honesty', 'C) Fairness', 'D) Transparency', 'A'),
        ('What is the term for a situation where a person or entity has a conflict of interest between personal and professional duties?', 'A) Dilemma', 'B) Conflict', 'C) Bias', 'D) Compromise', 'A'),
        ('Which ethical principle emphasizes treating others fairly and justly in business transactions?', 'A) Equity', 'B) Justice', 'C) Fairness', 'D) Equality', 'A'),
        ('What term describes the ethical responsibility of businesses to contribute positively to society and the environment?', 'A) Social responsibility', 'B) Environmental stewardship', 'C) Corporate citizenship', 'D) Sustainability', 'A'),
        ('What is the term for the practice of disclosing information that could influence a business transaction?', 'A) Transparency', 'B) Disclosure', 'C) Openness', 'D) Honesty', 'A'),
        ('Which ethical theory emphasizes the importance of maximizing overall happiness or well-being?', 'A) Utilitarianism', 'B) Deontology', 'C) Virtue ethics', 'D) Egoism', 'A'),
        ('What is the term for the unethical practice of using one\'s position or power for personal gain?', 'A) Bribery', 'B) Fraud', 'C) Corruption', 'D) Embezzlement', 'C'),
        ('Which ethical principle emphasizes the importance of keeping promises and fulfilling obligations?', 'A) Fidelity', 'B) Honesty', 'C) Integrity', 'D) Loyalty', 'A'),
        ('What is the term for the systematic evaluation of a company\'s activities and their impact on society and the environment?', 'A) Corporate social responsibility', 'B) Sustainability reporting', 'C) Triple bottom line', 'D) Social audit', 'B'),
        ('What ethical theory suggests that ethical decisions should be based on fundamental principles of right and wrong?', 'A) Deontology', 'B) Virtue ethics', 'C) Utilitarianism', 'D) Relativism', 'A')
    ]

    business_analytics = [
        ('What is the term for the process of analyzing historical data to predict future outcomes?', 'A) Forecasting', 'B) Regression', 'C) Data mining', 'D) Trend analysis', 'A'),
        ('What statistical measure is used to describe the dispersion or spread of data points in a dataset?', 'A) Variance', 'B) Mean', 'C) Standard deviation', 'D) Range', 'A'),
        ('What term describes the technique of using algorithms to extract patterns and insights from large datasets?', 'A) Data mining', 'B) Machine learning', 'C) Data wrangling', 'D) Data visualization', 'A'),
        ('What is the name of the statistical method used to identify relationships between variables in a dataset?', 'A) Regression', 'B) Correlation', 'C) Hypothesis testing', 'D) ANOVA', 'A'),
        ('What term refers to the process of cleaning and organizing data before analysis?', 'A) Data preprocessing', 'B) Data transformation', 'C) Data wrangling', 'D) Data cleansing', 'A'),
        ('Which type of analysis involves categorizing data into groups or clusters based on similarity?', 'A) Clustering', 'B) Regression', 'C) Classification', 'D) Association', 'A'),
        ('What is the name of the technique used to visualize data and identify patterns through graphical representations?', 'A) Data visualization', 'B) Data exploration', 'C) Data modeling', 'D) Data interpretation', 'A'),
        ('What statistical measure represents the central tendency of a dataset?', 'A) Mean', 'B) Median', 'C) Mode', 'D) Range', 'A'),
        ('What is the term for the process of identifying and correcting errors in data?', 'A) Data cleaning', 'B) Data validation', 'C) Data auditing', 'D) Data scrubbing', 'A'),
        ('What type of analysis focuses on identifying the factors that contribute most to a particular outcome?', 'A) Factorial', 'B) Regression', 'C) Correlation', 'D) ANOVA', 'A')
    ]

    econometrics = [
        ('What statistical technique is commonly used to estimate the relationship between variables in econometrics?', 'A) Regression', 'B) Correlation', 'C) Time series analysis', 'D) ANOVA', 'A'),
        ('What is the term for the phenomenon where a change in one variable causes a change in another variable?', 'A) Causality', 'B) Correlation', 'C) Endogeneity', 'D) Spurious correlation', 'A'),
        ('Which econometric model is used when the dependent variable is binary or categorical?', 'A) Logit', 'B) Probit', 'C) OLS', 'D) ARIMA', 'A'),
        ('What is the name of the method used in econometrics to correct for autocorrelation in time series data?', 'A) ARIMA', 'B) ARCH', 'C) GARCH', 'D) Heteroscedasticity', 'A'),
        ('What term describes the situation where the error term in a regression model has a mean of zero?', 'A) Homoscedasticity', 'B) Heteroscedasticity', 'C) Autocorrelation', 'D) Multicollinearity', 'A'),
        ('What type of analysis involves estimating the effect of one variable on another while holding other variables constant?', 'A) Partial', 'B) Marginal', 'C) Simultaneous', 'D) Conditional', 'A'),
        ('What is the name of the econometric technique used to estimate the joint effect of multiple independent variables on a dependent variable?', 'A) Multiple Regression', 'B) Time series analysis', 'C) Panel data analysis', 'D) Path analysis', 'A'),
        ('What term refers to the problem of using past data to predict future outcomes in econometrics?', 'A) Forecasting', 'B) Extrapolation', 'C) Overfitting', 'D) Data mining', 'A'),
        ('Which statistical test is used to determine whether there is a significant relationship between the independent and dependent variables in a regression model?', 'A) T-test', 'B) F-test', 'C) Chi-square test', 'D) Z-test', 'A'),
        ('What is the term for the method used to estimate parameters in a regression model by minimizing the sum of squared differences between observed and predicted values?', 'A) Least Squares', 'B) Maximum Likelihood', 'C) Ordinary Least Squares', 'D) Generalized Least Squares', 'A')
    ]

    insert_questions(business_strategy, "Business Strategy")
    insert_questions(entrepreneurship, "Entrepreneurship")
    insert_questions(business_ethics, "Business Ethics")
    insert_questions(business_analytics, "Business Analytics")
    insert_questions(econometrics, "Econometrics")
