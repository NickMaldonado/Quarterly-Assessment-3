from database_manager import DatabaseManager

def populate_database():
    db_manager = DatabaseManager("quiz_bowl.db")
    db_manager.connect()
    db_manager.create_table()

    business_strategy = [
        ('BusinessStrategy', 'What business strategy framework was introduced by Michael Porter in 1979?', 'Porter', 'Diversification', 'Strength', 'Penetration', 'Porter'),
        ('BusinessStrategy', 'What is the term for the strategy involving the development and introduction of new products or services into existing markets?', 'Diversification', 'Penetration', 'Strength', 'Porter', 'Diversification'),
        ('BusinessStrategy', 'In business strategy, what does the "S" in SWOT stand for?', 'Strength', 'Porter', 'Penetration', 'Diversification', 'Strength'),
        ('BusinessStrategy', 'What strategy involves a company lowering its prices to gain market share rapidly?', 'Penetration', 'Diversification', 'Porter', 'Strength', 'Penetration'),
        ('BusinessStrategy', 'Which strategic planning tool visualizes the competitive positions of companies in an industry?', 'Boston Matrix', 'Porter', 'Penetration', 'Diversification', 'Boston Matrix'),
        ('BusinessStrategy', 'What is the strategy where a company focuses on serving a specific segment of the market?', 'Niche', 'Boston Matrix', 'Penetration', 'Diversification', 'Niche'),
        ('BusinessStrategy', 'Which strategy focuses on reducing costs through efficient production and distribution processes?', 'Cost Leadership', 'Niche', 'Boston Matrix', 'Penetration', 'Cost Leadership'),
        ('BusinessStrategy', 'What is the term for a strategic alliance between two or more companies to achieve a common objective?', 'Partnership', 'Cost Leadership', 'Niche', 'Boston Matrix', 'Partnership'),
        ('BusinessStrategy', 'What is the strategic approach that aims to create a unique and valuable position in the market?', 'Differentiation', 'Partnership', 'Cost Leadership', 'Niche', 'Differentiation'),
        ('BusinessStrategy', 'What strategy involves a company expanding its operations into new markets or industries?', 'Expansion', 'Differentiation', 'Partnership', 'Cost Leadership', 'Expansion')
    ]

    entrepreneurship = [
        ('Entrepreneurship', 'Who is often regarded as the "father of modern entrepreneurship"?', 'Schumpeter', 'Chesky', 'Elon Musk', 'Gates', 'Schumpeter'),
        ('Entrepreneurship', 'What term describes a business model that seeks to address a social or environmental issue while generating profit?', 'Social', 'Schumpeter', 'Chesky', 'Elon Musk', 'Social'),
        ('Entrepreneurship', 'Which Silicon Valley entrepreneur co-founded PayPal and later became the CEO of Tesla and SpaceX?', 'Elon Musk', 'Social', 'Schumpeter', 'Chesky', 'Elon Musk'),
        ('Entrepreneurship', 'What is the term for a small amount of money invested in a startup in exchange for ownership equity?', 'Seed', 'Elon Musk', 'Social', 'Schumpeter', 'Seed'),
        ('Entrepreneurship', 'What is the name of the phenomenon where entrepreneurs take failed ideas or businesses and turn them into successful ventures?', 'Pivot', 'Seed', 'Elon Musk', 'Social', 'Pivot'),
        ('Entrepreneurship', 'What term describes the practice of bringing together resources to start a business venture?', 'Bootstrapping', 'Pivot', 'Seed', 'Elon Musk', 'Bootstrapping'),
        ('Entrepreneurship', 'Which entrepreneur famously dropped out of college to co-found Microsoft?', 'Gates', 'Bootstrapping', 'Pivot', 'Seed', 'Gates'),
        ('Entrepreneurship', 'What is the term for the process of strategically choosing which markets to enter with a new product or service?', 'Market', 'Gates', 'Bootstrapping', 'Pivot', 'Market'),
        ('Entrepreneurship', 'What is the name of the entrepreneur who co-founded Airbnb?', 'Chesky', 'Market', 'Gates', 'Bootstrapping', 'Chesky'),
        ('Entrepreneurship', 'What term describes the strategy of rapidly scaling a business by reinvesting profits rather than seeking external funding?', 'Organic', 'Chesky', 'Market', 'Gates', 'Organic')
    ]

    business_ethics = [
        ('BusinessEthics', 'What term refers to the ethical principle of being honest and truthful in business dealings?', 'Integrity', 'Transparency', 'Fidelity', 'Equity', 'Integrity'),
        ('BusinessEthics', 'What is the term for a situation where a person or entity has a conflict of interest between personal and professional duties?', 'Dilemma', 'Integrity', 'Transparency', 'Fidelity', 'Dilemma'),
        ('BusinessEthics', 'Which ethical principle emphasizes treating others fairly and justly in business transactions?', 'Equity', 'Dilemma', 'Integrity', 'Transparency', 'Equity'),
        ('BusinessEthics', 'What term describes the ethical responsibility of businesses to contribute positively to society and the environment?', 'Social', 'Equity', 'Dilemma', 'Integrity', 'Social'),
        ('BusinessEthics', 'What is the term for the practice of disclosing information that could influence a business transaction?', 'Transparency', 'Social', 'Equity', 'Dilemma', 'Transparency'),
        ('BusinessEthics', 'Which ethical theory emphasizes the importance of maximizing overall happiness or well-being?', 'Utilitarianism', 'Transparency', 'Social', 'Equity', 'Utilitarianism'),
        ('BusinessEthics', 'What is the term for the unethical practice of using one\'s position or power for personal gain', 'Corruption', 'Utilitarianism', 'Transparency', 'Social', 'Corruption'),
        ('BusinessEthics', 'Which ethical principle emphasizes the importance of keeping promises and fulfilling obligations?', 'Fidelity', 'Corruption', 'Utilitarianism', 'Transparency', 'Fidelity'),
        ('BusinessEthics', 'What is the term for the systematic evaluation of a company\'s activities and their impact on society and the environment?', 'Sustainability', 'Fidelity', 'Corruption', 'Utilitarianism', 'Sustainability'),
        ('BusinessEthics', 'What ethical theory suggests that ethical decisions should be based on fundamental principles of right and wrong?', 'Deontology', 'Sustainability', 'Fidelity', 'Corruption', 'Deontology')
    ]

    business_analytics = [
        ('BusinessAnalytics', 'What is the term for the process of analyzing historical data to predict future outcomes?', 'Forecasting', 'Data Cleansing', 'Regression', 'Data Mining', 'Forecasting'),
        ('BusinessAnalytics', 'What statistical measure is used to describe the dispersion or spread of data points in a dataset?', 'Variance', 'Forecasting', 'Data Cleansing', 'Regression', 'Variance'),
        ('BusinessAnalytics', 'What term describes the technique of using algorithms to extract patterns and insights from large datasets?', 'Data Mining', 'Variance', 'Forecasting', 'Data Cleansing', 'Data Mining'),
        ('BusinessAnalytics', 'What is the name of the statistical method used to identify relationships between variables in a dataset?', 'Regression', 'Data Mining', 'Variance', 'Forecasting', 'Regression'),
        ('BusinessAnalytics', 'What term refers to the process of cleaning and organizing data before analysis?', 'Data Preprocessing', 'Regression', 'Data Mining', 'Variance', 'Data Preprocessing'),
        ('BusinessAnalytics', 'Which type of analysis involves categorizing data into groups or clusters based on similarity?', 'Clustering', 'Data Preprocessing', 'Regression', 'Data Mining', 'Clustering'),
        ('BusinessAnalytics', 'What is the name of the technique used to visualize data and identify patterns through graphical representations?', 'Data Visualization', 'Clustering', 'Data Preprocessing', 'Regression', 'Data Visualization'),
        ('BusinessAnalytics', 'What statistical measure represents the central tendency of a dataset?', 'Mean', 'Data Visualization', 'Clustering', 'Data Preprocessing', 'Mean'),
        ('BusinessAnalytics', 'What is the term for the process of identifying and correcting errors in data?', 'Data Cleansing', 'Mean', 'Data Visualization', 'Clustering', 'Data Cleansing'),
        ('BusinessAnalytics', 'What type of analysis focuses on identifying the factors that contribute most to a particular outcome?', 'Factorial', 'Data Cleansing', 'Mean', 'Data Visualization', 'Factorial')
    ]

    econometrics = [
        ('Econometrics', 'What statistical technique is commonly used to estimate the relationship between variables in econometrics?', 'Regression', 'Least Squares', 'T-test', 'Forecasting', 'Regression'),
        ('Econometrics', 'What is the term for the phenomenon where a change in one variable causes a change in another variable?', 'Causality', 'Regression', 'Least Squares', 'T-test', 'Causality'),
        ('Econometrics', 'Which econometric model is used when the dependent variable is binary or categorical?', 'Logit', 'Causality', 'Regression', 'Least Squares', 'Logit'),
        ('Econometrics', 'What is the name of the method used in econometrics to correct for autocorrelation in time series data?', 'ARIMA', 'Logit', 'Causality', 'Regression', 'ARIMA'),
        ('Econometrics', 'What term describes the situation where the error term in a regression model has a mean of zero?', 'Homoscedasticity', 'ARIMA', 'Logit', 'Causality', 'Homoscedasticity'),
        ('Econometrics', 'What type of analysis involves estimating the effect of one variable on another while holding other variables constant?', 'Partial', 'Homoscedasticity', 'ARIMA', 'Logit', 'Partial'),
        ('Econometrics', 'What is the name of the econometric technique used to estimate the joint effect of multiple independent variables on a dependent variable?', 'Multiple Regression', 'Partial', 'Homoscedasticity', 'ARIMA', 'Multiple Regression'),
        ('Econometrics', 'What term refers to the problem of using past data to predict future outcomes in econometrics?', 'Forecasting', 'Multiple Regression', 'Partial', 'Homoscedasticity', 'Forecasting'),
        ('Econometrics', 'Which statistical test is used to determine whether there is a significant relationship between the independent and dependent variables in a regression model?', 'T-test', 'Forecasting', 'Multiple Regression', 'Partial', 'T-test'),
        ('Econometrics', 'What is the term for the method used to estimate parameters in a regression model by minimizing the sum of squared differences between observed and predicted values?', 'Least Squares', 'T-test', 'Forecasting', 'Multiple Regression', 'Least Squares')
    ]

    # Insert questions into the database
    for question in business_strategy:
        db_manager.insert_question(*question)

    for question in entrepreneurship:
        db_manager.insert_question(*question)

    for question in business_ethics:
        db_manager.insert_question(*question)

    for question in business_analytics:
        db_manager.insert_question(*question)

    for question in econometrics:
        db_manager.insert_question(*question)

    db_manager.close_connection()

if __name__ == "__main__":
    populate_database()
