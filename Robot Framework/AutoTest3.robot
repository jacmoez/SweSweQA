*** Settings ***
Library             SeleniumLibrary


*** Variables ***
${url}             https://testautomationpractice.blogspot.com/

${dobule}          //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[7]/div[1]/button

${slider1}        //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[9]/div[1]/div/span[1]

${slider2}        //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[9]/div[1]/div/span[2]

${drop_down}     //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[11]/div[1]/div/div[10]

${home}          //html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[2]/div/ul/li[1]/a

${hidden}       //html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[2]/div/ul/li[2]/a



${download_pdf}    //html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div[1]/div[2]/button[3]

*** Keywords ***
Testing
     Sleep                                           5
     Double Click Element                           ${dobule}
     Sleep                                           5
     ${text}=             Get Text                    id:field2
     Log                  ${text}
     Drag and Drop        id:draggable              id:droppable
     Sleep                3
     Drag And Drop By Offset                        ${slider1}             -75         0
     Drag And Drop By Offset                        ${slider2}              -100        0
     Sleep                                          3
     Input Text             id:comboBox             Item 10
     Sleep                  2
     Click Element          ${drop_down}
      Sleep                 2
      Click Element         id:apple
      Sleep                 4
      Execute JavaScript    window.history.back()
      Sleep                 2
      Click Element         id:lenovo
      Sleep                 4
      Execute JavaScript    window.history.back()
      Sleep                 2
      Click Element        id:dell
      Sleep                4
      Execute JavaScript   window.history.back()
      Sleep                2
      FOR        ${i}       IN RANGE            1       8
                 Click Element      //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[12]/div[1]/div/div[3]/a[${i}]
                 Sleep              2
                 ${title}=          Get Title
                 Log                ${title}
                 Execute JavaScript          window.history.back()
                 Sleep              5
      END

Form
    ${elements}                 Create List                 Swe Swe      Wai Wai     Hla Hla

    FOR         ${i}            IN RANGE                    0           3
                ${count}=       Evaluate                    ${i} + 1
                Input Text      id:input${count}            ${elements}[${i}]
                Sleep           3
                Click Button    id:btn${count}
                Sleep           3

    END
    Click Element               ${home}
    Sleep                       3
    Click Element               ${hidden}
    Click Button                id:toggleInput
    ${text}=        Get Text                id:statusLabel
    Log             ${text}
    Sleep           2
    Click Button    id:toggleCheckbox
    ${text}=        Get Text                id:toggleCheckbox
    Sleep           2
    Click Button    id:loadContent
    ${text}=        Get Text                id:toggleCheckbox
    Click Element           /html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[2]/div/ul/li[3]/a

#Download Files
    Click Element          /html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[2]/div/ul/li[3]/a
    Sleep                   3
#    Input Text              id:inputText              QA Swe Swe
#    Sleep                   3
#    Click Button            id:generateTxt
#    Sleep                   3
#    Click Element           id:txtDownloadLink
#    Sleep                   3
#    Click Button            id:generatePdf
#    Sleep                   3
#    Click Element           id:pdfDownloadLink
#    Sleep                   3
#    Clickc Button           ${download_pdf}
#    Sleep                   3


*** Test Cases ***
Main
    Open Browser            ${url}                  browser=Edge
    Maximize Browser Window
    #Testing
    Form
    #Download Files
    Sleep                   5