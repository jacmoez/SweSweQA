*** Settings ***
Library                     SeleniumLibrary

*** Variables ***
${url}                      https://web-staging.renonation.sg/

${Loginbtn}         xpath:/html/body/div/div/div[2]/div/header/div/div[2]/div/button[2]

${Mobiletxt}        xpath:/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/div/div/input

${MobileNextbtn}    xpath:/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/button/span

${mobile_err}       xpath:/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/p/span

${otp_box}        //html/body/div/div/div[3]/div/div/form[2]/div/div/fieldset/div/div[2]/input

${otp_btn}      //html/body/div/div/div[3]/div/div/form[2]/div/div/button

${setp1_btn}   //html/body/div/div/main/div/div/div[2]/div/div[2]/button

${dbss_btn}     //html/body/div/div/main/div/form[2]/div/div[2]/div/div[1]/div/fieldset[1]/div/button[3]

${new}       //html/body/div/div/main/div/form[2]/div/div[2]/div/div[1]/div/fieldset[2]/div/button[1]
*** Keywords ***
Renovation Login
           Sleep               5s
           Click Button        ${Loginbtn}
           Sleep               5s
           Input Text          ${Mobiletxt}            8311
           Sleep               5s
           Press Keys          ${MobileNextbtn}        RETURN
           Sleep               3s
           ${errortext}=       Get Text               ${mobile_err}

           Sleep                       3s
           log                        ${errortext}
           Clear Element Text         ${mobiletxt}
           Input Text                 ${mobiletxt}      83119908
           Sleep                       3
           Click Element               ${MobileNextbtn}
           Sleep                      5
           Input Text                 name:otp               232323
           Sleep                      3
           Click Button               ${otp_btn}
           Sleep                      3
           Input Text                  id:firstName             QA
           Sleep                      3
           Input Text                 id:lastName               Swe Swe
           Sleep                       3
           Input Text                 id:email                  swe@21.com
           Sleep                      3
           Click Button               ${setp1_btn}
           Sleep                       3
           Click Button               ${dbss_btn}
           Sleep                       5




*** Test Cases ***
Main
   Open Browser            ${url}           browser=Chrome
   Maximize Browser Window
   Renovation Login
   Sleep                   5