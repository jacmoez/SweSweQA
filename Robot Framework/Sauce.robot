*** Settings ***

Library             SeleniumLibrary
Suite Setup         Open Browser  ${url}    ${browser}
Suite Teardown      Close Browser

*** Variables ***
${url}          https://www.saucedemo.com/
${browser}      Chrome


*** Test Cases ***
Login With Valid
        Input Text          id=user-name        standard_user
        Sleep               2s
        Input Text          id=password         secret_sauce
        Press Keys          id=password          RETURN
        Sleep               2s


Check Inventory Page
    Page Should Contain     Products
    Sleep                   2s


Add Item To Cart
     Click Button          id=add-to-cart-sauce-labs-backpack
     Sleep                 2s
     Click Button          id=add-to-cart-sauce-labs-fleece-jacket
     Sleep                 2s
     Click Button          name=add-to-cart-test.allthethings()-t-shirt-(red)
     Sleep                 2s

Remove Item From Cart

        Click Button      id=remove-sauce-labs-fleece-jacket
        Sleep             2s

View Cart
    Click Element         class=shopping_cart_link
    Sleep                 2s
    Page Should Contain   Your Cart
    Click Element         xpath=/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div
    Sleep                 2s

Remove Item From Cart
    Click Element         class=shopping_cart_link
    Sleep                 2s
    Click Button          id=remove-sauce-labs-backpack
    Sleep                 2s


Process To Checkout
    Click Button        id=checkout
    Sleep               2s


Checkout Information
    Input Text          id=first-name        QA
    Sleep               2s
    Input Text          id=last-name        Testing
    Sleep               2s
    Input Text          id=postal-code         11111
    Sleep               2s
    Click Button        xpath=//*[@id="continue"]
    Sleep               2s


Verify Payment
    ${item_total}=       Get Text            class=summary_subtotal_label
    ${tax_total}=        Get Text            class=summary_tax_label
    ${total_price}=      Get Text            class=summary_total_label
    Sleep                2s
    Log      Item Total: ${item_total}
    Log      Tax: ${tax_total}
    Log       Total: ${total_price}

Finish Checkout
        Click Button    css=.btn.btn_action.btn_medium.cart_button
        Sleep           5s