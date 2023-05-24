# README

This Python script provides an interface to interact with a specific web application. It uses Selenium WebDriver to automate various interactions with the website, such as clicking on elements, waiting for elements to be present, waiting for elements to become invisible, and sending input to elements. In addition, it includes functions to navigate the website, such as login, get link texts, remove previous lists, load patient recipients, and create campaigns.
Prerequisites

    Python 3.x
    Selenium WebDriver
    Internet access (The script interacts with a web application)

Dependencies

    Selenium
    Time

Functions

    click_element(method, target): This function clicks on a web element. The method and target are used to locate the element.

    present_element(method, target, input): This function waits until a web element is present and sends input to it. The method and target are used to locate the element.

    all_elements(method, target): This function waits until all elements are located and then returns these elements. The method and target are used to locate the elements.

    invisible_wait(method, target): This function waits for a web element to become invisible. The method and target are used to locate the element.

    login(username, password): This function logs into the website using the given username and password.

    get_link_texts(company, closed_clinics): This function clicks on a user element, gets all options related to a company, and removes deactivated clinics. It also removes any closed clinics provided.

    remove_previous_lists(driver, recipient, recipient_list): This function attempts to click on the CRM link and the Recipient Lists link. It removes previous lists related to the recipient.

    patient_recipient_load(driver, recipient, three_months, recipient_list): This function loads patient recipients for a specified recipient and recipient list. It applies a three-month filter.

    create_campaign(driver, email_campaign_name, subject, email_body, recipient_list): This function creates an email campaign. It requires parameters for the campaign name, subject, body, and recipient list.

