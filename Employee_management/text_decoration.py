import fontstyle

def text_decorate():
    text = fontstyle.apply('EMPLOYEE MANAGEMENT SYSTEM', 'bold/Italic/red/GREEN_BG')
    total_width = 130
    left_padding = (total_width - len(text)) // 2
    centered_text = " " * left_padding + text
    print(centered_text)
    company_info = '\nWelcome to Watchguard, where innovation meets security. We are dedicated to providing seamless access to your digital world while safeguarding your data. Join us and experience the future of secure connectivity.\n'
    text = fontstyle.apply(company_info, 'Italic/black,WHITE_BG')
    print(text)