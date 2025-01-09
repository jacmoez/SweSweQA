*** Settings ***
Library             SeleniumLibrary


*** Variables ***
${url}              https://testautomationpractice.blogspot.com/
${img1}             C:\\Users\\DELL\\Pictures\\backgound.jpeg
${img2}             C:\\Users\\DELL\\Pictures\\Screenshots\\Screenshot 2024-12-28 001548.png
${newtab}           xpath:/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[4]/div[1]/button
${mobile}           xpath:/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[6]/div[1]/div/div/a[1]

*** Keywords ***
Input Filed Test
#     Input Text             id=name                     Automation
#     Sleep                  2s
#
#     Input Text             css:input[placeholder="Enter EMail"]    sweswe@yopmail.com
#     Sleep                  2s
#     Input Text             id=phone                    09473878234
#     Sleep                  2s
#     Clear Element Text     id=phone
#     Sleep                  2s
#     Input Text             id=phone                    09778656503
#     Input Text             xpath=//*[@id="textarea"]   Yangon,Myanmar.
#     Sleep                  2s

    ${element}=         Get WebElements         css:input[placeholder^="Enter"]

    ${user_data}=       Create List             QA      qa@ams.com.mm   9778656503

    FOR     ${i}        IN RANGE                0    3
                        Input Text              ${element}[${i}]    ${user_data}[${i}]
                        Sleep                   2s
    END
    Input Text          id:textarea             Yangon, Myanmar.

Readio Test
    Click Element                       css:input[value="male"]
    Sleep                               2s

Checkbox Test
    ${days}=                  Create List            sunday       tuesday         friday
    FOR     ${i}                IN RANGE                0           3
                              Click Element          id=${days}[${i}]
                              Sleep                  2s
    END


Select Test
    Select From List By Value           id=country       japan
    Sleep                               2s
    Select From List By Value           id=colors        red        yellow
    Sleep                               2s
    Select From List By Value           id=animals       dog       cat
    Sleep                               2s

Date Picker Test
        Input Text              id=datepicker           03/29/1994
        Press Keys              id=datepicker           RETURN
        Sleep                   2s
        Click Element           id=txtDate
        Sleep                   2s
        Click Element           xpath:/html/body/div[5]/table/tbody/tr[3]/td[4]/a
        Sleep                   2s
        Input Text              id:start-date           03/29/1994
        Sleep                   2s
        Input Text              id:end-date             01/03/2025
        Sleep                   2s
        Click Button            class=submit-btn
        Sleep                   2s
        ${result}=              Get Text                id=result
        Log                  life day: ${result}
        Click Element           class=home-link
        Sleep                   2s

File Upload
    Choose File                     id=singleFileInput          ${img1}
    Sleep                           2s
    Click Button                    xpath=/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[2]/div[1]/form[1]/button
    Sleep                           2s
    Choose File                     id=multipleFilesInput       ${img1}\n${img2}
    Sleep                           2s
    Click Button                    xpath=/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[2]/div[1]/form[2]/button
    Sleep                           2s

Table Data
    Table Data By Name                          BookTable
    Table Data By ID                            taskTable
    #Table Data By ID With Checkbox
    #Pageination Table
    Click Check For One Page Using Step

Table Data By Name
    [Arguments]                                 ${table_name}
    #First Way
    @{cells}=       Get WebElements             xpath://table[@name='${table_name}']//td
    FOR              ${cell}      IN             @{cells}
                     ${text}=     Get Text       ${cell}
    END

    #Second Way
    @{rows}=        Get WebElements             xpath://table[@name='${table_name}']//tr
    FOR             ${row}        IN            @{rows}
                    ${row_elemets}=             Get WebElements     ${row}
                    ${text}=                    Get Text            ${row_elemets}
    END

 #Dynamic Web Table
Table Data By ID
    [Arguments]                                 ${table_id}
    @{cells}=           Get WebElements          xpath://table[@id='${table_id}']//td
    FOR       ${cell}           IN               @{cells}
               ${text}=       Get Text           ${cell}
    END

#Pagination Web Table

Table Data By ID With Checkbox
        FOR            ${i}        IN RANGE            1         6
                                   Click Element       xpath:/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[${i}]/td[4]/input
                      Sleep        1s
        END

Pageination Table
        @{elements}=                Get WebElements              xpath://*[@id="pagination"]/li/a
        FOR     ${i}                IN                           @{elements}
                                    Click Element                 ${i}
                                    Table Data By ID With Checkbox
                                    Sleep                        1s
        END


Click Check For One Page Using Step
        FOR         ${i}        IN RANGE         1      6       2
                    Click Element                //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[${i}]/td[4]/input

        END

Search Text
        Input Text                            id:Wikipedia1_wikipedia-search-input              Robot Framework

        Press Keys                             class:wikipedia-search-input                     RETURN


Dynamic Button
        Click Element                         name:start

        Sleep                                   2s
        Click Button                           name:stop
        Sleep                                  2s

Alerts
      Click Button                             id:alertBtn
      Sleep                                    2s
      Handle Alert
      Sleep                                    2s
      Click Button                             id:confirmBtn
      Sleep                                    2s
      Handle Alert                             accept
      Sleep                                    2s
#      Click Element                            id:promptBtn
#      Sleep                                    5s

New Tab
      Click Button                           ${newtab}
      Sleep                                   2s
      ${handle}=                             Get Window Handles
      Switch Window                         ${handle}[1]
      Sleep                                  3s
      Close Window
      Switch Window                         ${handle}[0]
      Sleep                                  2s
#      Click Button                          id:PopUp
#      Sleep                                 2s

Hover Point Me
      Click Button                         class:dropbtn
      Sleep                                2s
      #Mobile
      Scroll Element Into View             ${mobile}
      Sleep                                5s


Fields
     Input Text                             id:field1                   QA
     Sleep                                  2s
     Click Button                           //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[7]/div[1]/button
     Sleep                                  2s

*** Test Cases ***
Main
     Open Browser       ${url}           browser=Edge
     Maximize Browser Window
#     Input Filed Test
#     Readio Test
#     Checkbox Test
#     Select Test
#     Date Picker Test
#     File Upload
      Table Data
      Search Text
      Dynamic Button
      Alerts
      New Tab
      Hover Point Me
      Fields