*** Settings ***
Library         SeleniumLibrary

*** Variables ***
${url}                           https://web-staging.renonation.sg/
${start_number}                     8311
${total_length}                     8
${mail}                           @yopmail.com

${login_btn}                       //html/body/div/div/div[2]/div/header/div/div[2]/div/button[2]
${mobile_text}                     //html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/div/div/input
${mobile_btn}                      //html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/button
${otp_btn}                         //html/body/div/div/div[3]/div/div/form[2]/div/div/button

${setone_btn}                      //html/body/div/div/main/div/div/div[2]/div/div[2]/button

*** Keywords ***
Login
    Sleep                                       4
    Click Element                                ${login_btn}
    Sleep                                           4
    Input Text                                  ${mobile_text}          ${start_number}
    Sleep                                       4
    Click Button                                ${mobile_btn}

verify Invalid Message
    ${msg}=                                     Get Text                css:.flex-1.text-sm.text-error
    Log                                         ${msg}

Input Mobile Numbre Random
    ${mobile_length}=         Evaluate          ${total_length} - len(str(${start_number}))
    ${random_digits}=         Evaluate          "".join(map(str, random.choices(range(10), k=${mobile_length} )))    random
    ${final_number}=          Set Variable      ${start_number}${random_digits}
    Log                        ${final_number}
    Input Text                ${mobile_text}                ${final_number}
    Sleep                       3
    Click Button                ${mobile_btn}
    Sleep                       3
    Input Text                  name:otp                    232323
    Sleep                       3
    Click Button               ${otp_btn}
    Sleep                       5
    Input Text                 id:firstName                QA
    Sleep                       5
    Input Text                  id:lastName                 Swe Swe
    Sleep                       5


    ${email}=                    Set Variable         sweswe${random_digits}${mail}
    Sleep                        3
    Input Text                  id:email                    ${email}
    Sleep                       3
    Click Button                ${setone_btn}

*** Test Cases ***
Main
     Open Browser               ${url}              browser=Edge
     Maximize Browser Window
     Login
     verify Invalid Message
     Input Mobile Numbre Random
     Sleep                      5
