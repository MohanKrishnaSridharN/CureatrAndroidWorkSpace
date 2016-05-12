CureatrPlayURL="https://cureatr-vm.dev:5101/"
#CureatrPlayURL="https://messenger.play.cureatr.com"
EmailAccountsForReports="nmksridhar@gmail.com"
#EmailAccountsForReports=esheddoni@cureatr.com|levimcdonough@cureatr.com|kiran.gopisetty@mtuity.com

"""
#MAC URLS
LOG_FILE="/Users/macmini/Cureatr/CureatrPythonWorkSpace/applicationlogs/applog.txt"
OutPutFileDir="/Users/macmini/Cureatr/CureatrPythonWorkSpace/OutPutFiles/"
Suite_Web="/Users/macmini/Cureatr/CureatrPythonWorkSpace/InputFiles/Web/Suite_Web.xlsx"
Results="/Users/macmini/Cureatr/CureatrPythonWorkSpace/InputFiles/Web/Results.xlsx"
InPutFileDir="/Users/macmini/Cureatr/CureatrPythonWorkSpace/InputFiles/Web/"


#Windows URLS
LOG_FILE="D:/CureatrPythonWorkSpace/applicationlogs/applog.txt"
OutPutFileDir="D:/CureatrPythonWorkSpace/OutPutFiles/"
Suite_Web="D:/CureatrPythonWorkSpace/InputFiles/Web/Suite_Web.xlsx"
Results="D:/CureatrPythonWorkSpace/InputFiles/Web/Results.xlsx"
InPutFileDir="D:/CureatrPythonWorkSpace/InputFiles/Web/"
"""
#UBUNTU
LOG_FILE="/home/cureatr/CureatrPythonWorkSpace/applicationlogs/applog.txt"
OutPutFileDir="/home/cureatr/CureatrPythonWorkSpace/OutPutFiles/"
Suite_Web="/home/cureatr/CureatrPythonWorkSpace/InputFiles/Web/Suite_Web.xlsx"
Results="/home/cureatr/CureatrPythonWorkSpace/InputFiles/Web/Results.xlsx"
InPutFileDir="/home/cureatr/CureatrPythonWorkSpace/InputFiles/Web/"

verifyTitle="Cureatr Messenger"

#Home Screen Objects xpath
WelcomeMsg="//h1"
GetSupportMsg="//a"
InfoMsg="//*[@id='frame']/div/div[1]/div/div[2]"
OrgWaterMark="//*[@id='institution-input']"
InstTextBox="//*[@id='institution-input']"
InstSelection="//*[@id='frame']/div/div[2]/div[2]/div/div/div/div[1]/div[2]/ul/li"
CureatrIncMsg="//div[@id='frame']/div/div/div/div[4]"
SignInBtn="//*[@id='bigButtonText']"
Email="//*[@id='emailInput']"
Password="//*[@id='passwordInput']"

SignIn="//div[2]/div/div/div/div[2]/div"
ErrorMsg="//*[@id='frame']/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[2]"
ResetPasswordLink="//*[@id='resetPassword']"
SignUpLink="//*[@id='signUp']"         
ChangeOrg="//*[@id='changeOrg']"  
CureatrIncText="//*[@id='frame']/div/div[1]/div/div[4]"      
CureatrTextMsg="//*[@id='frame']/div/div[1]/div/div[2]"
GetSupportLink="//*[@id='frame']/div/div[1]/div/div[3]/a"
SelectedOrgName="//*[@id='frame']/div/div[2]/div[2]/div/div/div/div[1]/h1"
SignInBtnLink="//*[@id='frame']/div/div[2]/div[2]/div/div/div/div[2]"
EmailPlaceHolder="//input[@placeholder='Email address']"
PasswordPlaceHolder="//input[@placeholder='Password']"
LoginImage="//*[@id='loginImage']"
NavigationColumn1="//*[@id='navigation-column']/div[2]/div/div[4]/h2"
NavigationColumn2="//*[@id='navigation-column']/div[2]/div/div[4]/p"
ExistingAccount="//*[@id='existingAccount']"

ContactsLink="//*[@id='contacts-link']"

    
#Dashboard
UserName="//div[@id='header-user']/div/div/div/span"
InboxLink="//*[@id='inbox-link']"
ContactsLink="//*[@id='contacts-link']"
PatientsLink="//*[@id='patients-link']"
Settings="//*[@id='settings-link']"
SettingsID="settings-link"
Compose="//div[@id='navigation-column']/div/div/div/div/span"
ArchiveMultiple="//*[@id='navigation-column']/div[1]/div/div/div[2]/span"
EventsLink="//*[@id='events-link']"
StatusIcon="//*[@id='status-icon']"
Logo="//*[@id='logo']"
MainContent1="//*[@id='main-content']/div/h2"
MainContent2="//*[@id='main-content']/div/div[3]"
MainContentImg="//*[@id='main-content']/div/div[1]/img"
SignOutLink="//*[@id='header-user']/div/div[2]/div[2]/div[2]/a"



#Settings
settingsDropdown="//ul/div/div/div[2]"
ShowArchived="//*[@id='settingsDropdown']/div/div[1]/div[1]/label"


#Quick Message Screen
QuickMsgIcon="//div[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div/div[2]/div[2]/div[2]/div"
EditList="//a[contains(text(),'Edit list')]"
QuickMsgAddBtn="//li/div[2]/div[2]/span"
QuickMsgTextBox="//form/textarea"
QuickMsgSaveBtn="//a[contains(text(),'Save')]"
QuickMsgHeader="div.modal-header.clearfix > div.modal-title.truncate-text"
QuickMsgDialogClose="div.modal-close.cancel"

#New Message
NewMsgTitle="//*[@id='content']/div[3]/div/div/div[2]/div/div/div[1]"
NewMsgClose="//*[@id='content']/div[3]/div/div/div[2]/div/div/div[2]/div[2]"
NewMsgMinimize="//*[@id='content']/div[3]/div/div/div[2]/div/div/div[2]/div[1]"
ToLabel="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[1]/div/div[1]/label"
PatientLabel="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[2]/div/div[1]/label"
WorkflowLabel="//*[@id='workflow-select-view']/div[1]/label"
SubjectLabel="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[5]/label"
PressEnterToSend="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[3]/div[2]/label/span"
To="//*[@id='new-thread-to']"
SelectRecipient="//span/div[1]/div/div[2]/div"
Patient="//*[@id='new-thread-patient']"
Workflow="//*[@id='new-thread-workflow']"
ClickRecipientInTo="//fieldset/div/div/div/div/div/ul/li/div"
RemoveRecipientInTo="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[1]/div/div[1]/div/div/ul/li[1]/a"
Subject="//*[@id='new-thread-subject']"
MsgBody="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[2]/div[1]/textarea"
SendBtn="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[2]/div[2]/div[1]/div"
MsgBodyPart="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[2]/div[1]/div[2]/div[2]/div[2]"
SubjectPart="//*[@id='main-content']/div/div[1]/div/div[2]/div"
FileInputButton="//div[@id='fileinput-button']/input"
UrgentMessage="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[1]/div[2]/div/label"
FileUpload="//*[@id='fileinput-button']/label"
QuickMsgHelpText="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[2]/div/div/div[3]/div[2]"
QuickMsgCancelBtn="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[2]/div/div/div[3]/div[3]/a"
EditListBtn="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[2]/div/div/div[3]/div[1]/a"

PatientName="//*[@id='main-content']/div/div[1]/div/div[2]/div"
ConversationWith="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[1]/div/div/div"
ReadRecipt="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[2]/div[2]/div/span"
SentTime="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[2]/div[2]/div/div"
MsgBodyPartTextArea="//*[@id='main-content']/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/textarea"
QuickMsgIcon2="//*[@id='main-content']/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]"

NotificationIcon="//*[@id='eventsDropdown']/div/div[1]"


#CHAT THREAD
ChatThread="//*[@id='thread-collection']/li[1]/div[2]/div[2]/div[1]/div[1]"
ReplyMsgBody="//*[@id='main-content']/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/textarea"
LatestMsgBodyPart="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[3]/div[1]/div[2]/div[2]/div[2]"
ReplySendBtn="//*[@id='main-content']/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[1]/div"
ReplySendBtn2="//div[2]/div/div/div[2]/div[3]/div[2]"

#CONVERSATION SETTINGS
ConversationSettings="//*[@id='main-content']/div/div[1]/div/div[1]/div"
AddRecipient="//*[@id='threadSettingsModal']/div[2]/div[1]/div[1]/div[1]"
AddTextBox="//*[@id='addRecipientInput']"
SaveChanges="//*[@id='threadSettingsModal']/div[3]/div/a"
LeaveConversation="//*[@id='threadSettingsModal']/div[2]/div[3]"
ConfirmLeaveConversation="//a[contains(text(),'Leave conversation')]"
ArchivCheckBox="//*[@id='bottomCheckboxActions']/div/div[1]/label"
CloseConversationSettings="//*[@id='threadSettingsModal']/div[1]/div[2]/div"
Mute="//*[@id='bottomCheckboxActions']/div/div[2]/label"

#Profile
ProfileImg="//img[@id='current-user-profile-image']"
CloseProfileDialog="//*[@id='header-user']/div/div[2]/div[3]"
SignOut="//a[contains(text(),'Sign out')]"
PopUpSignOut="(//a[contains(text(),'Sign out')])[2]"
PopUpCancel="//a[contains(text(),'Cancel')]"
PopUpClose="div.modal-close"
PopUpCloseXpath="//div[6]/div/div/div/div[2]/div"
PopUpHeader="div.modal-title.truncate-text"
PopUpHeaderText="//div[6]/div/div/div/div"
PopUPText="//div[2]/p"
ArrowDropdown="//*[@id='header-user']/div/div[1]/div[4]"
Available="//label[1]/div"
Busy="//label[2]/div"
OffDuty="//label[3]/div"
ProfileDailog="//button[@type='button']"

#CHANGE PASSWORD
Close="//div/div/div/div[1]/div[1]/div[2]/div"
NewPasswordTextBox="//*[@id='js-new-pass-input']"
NewPasswordLabel="//div[1]/div[4]/div[2]/div[1]"
ReTypePasswordTextBox="//*[@id='new-pass-input-two']"
ReTypePasswordLabel="//div[1]/div[4]/div[3]/div"
ChangePasswordHelpText="//div/div/div/div[1]/div[4]/div[4]"
SaveChangesLink="//*[@id='change-password-link']"
ChangePassworHeader="div.modal-title.truncate-text"
CPWErrorMessage="//div/div/div/div[1]/div[2]/div[2]"
ErrorMsgText="div.password-message-contents"
CPWMainText="div.change-password-message"
StrengthMeterText="//div[4]/div[2]/div[2]/div[3]"
PWStreanghtBar1="//div[4]/div[2]/div[2]/div[1]"
PWStreanghtBar2="//div[4]/div[2]/div[2]/div[2]"
TSSignOut="//*[@id='tos_update']/div/div[1]/div[3]/div[1]/a"
TSAccept="//*[@id='tos_update']/div/div[1]/div[3]/div[2]/a"
TSHeader="div.modal-title.truncate-text"
TSXMark="//*[@id='tos_update']/div/div[1]/div[1]/div[2]/div"
TSInstructions="//*[@id='tos_instructions']"
TSContent="//*[@id='content']"