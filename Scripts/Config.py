#CureatrPlayURL="https://cureatr-vm.dev:5101/"
CureatrPlayURL="https://messenger.play.cureatr.com/"

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
ManageGroups="//*[@id='settingsDropdown']/div/div[1]/div[6]/div"
CreateGroupLink="//*[@id='createGroupLink']"
GroupNameInput="//*[@id='groupNameInput']"
CreateGroup="//*[@id='createGroup']"
AddRecipientInGroup="//div/div[1]/div[1]/div[1]"
AddRecipientInGroupCss="div.add-recipient"
#="//*[@id='addRecipientInput']"

#ContactsLink
ContactsSearch="//*[@id='directory_lookup']"
Contact="//*[@id='directory-lookup-results']/div[1]/div[2]/div[1]"
UserStatus="//div[1]/div[1]/div/div[3]/span"
UserStatusMsg="//div[1]/div[2]/div[3]/div[1]"
UserSpecialty="//div[1]/div[2]/div[3]/div[2]"
UserTitle="//div[1]/div[2]/div[3]/div[3]"
SendMsgLink="//div/div[2]/div/div[2]/div/a"
ShowMoreLink="//div[1]/div[5]/div/div/a"
NoContactMsg1="//*[@id='directory-lookup-results']/div[1]/h2"
NoContactMsg2="//*[@id='directory-lookup-results']/div[1]/div"
#UserService=""

#Patients Link
ComposeLinkAtPatients="//*[@id='directory-lookup-results']/div[1]/div/div[1]"
SelectPatient="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[2]/div/div[1]/div/div[1]/ul/li/div"

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
SelectedRecipient="//fieldset/div[1]/div/div[1]/div/div/ul/li[1]/div[1]"
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
QuikckMsgBtn="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[2]/div[2]/div[2]"
QuickMsgHelpText="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[2]/div/div/div[3]/div[2]"
QuickMsgCancelBtn="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[2]/div/div/div[3]/div[3]/a"
EditListBtn="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[2]/div/div/div[3]/div[1]/a"
AttachmentLink="//*[@id='fileinput-button']/label[2]"


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
CSClearSearch="//*[@id='threadSettingsModal']/div[2]/div[4]/div/div/div[1]/div[3]"
MGClearSearchCss="div.thread-action-cancel"

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
CurrentCoverage="//*[starts-with(@id, 'coverage-lookup-')]"
EditProfileCurrentCoverage="//div/div[1]/div/div[3]/form/div[2]/div[3]/div/div/div[2]/div/ul/li/input"
ViewYourProfile="//*[@id='header-user']/div/div[2]/div[2]/div[2]/span/a"
EditYourProfile="//div/div[2]/div/div[2]/a[2]"

CurrentService="//*[@id='current-service-view']/div/div[2]/div[2]"
ServiceSearchBar="//*[@id='service-search-bar']"
CurrentServiceView="//div/div[1]/div/div[3]/form/div[2]/div[5]/div[2]/div/div/div[2]/div[2]"


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

#contacts search xpath parts
cpath0="//*[@id='directory-lookup-results']/div"
cpath1="//*[@id='directory-lookup-results']/div["
cpath2="]/div[2]/div[1]"
cpath3="]/div[2]/div[4]"
DefaultLength1=0
Contacts=[cpath0, cpath1, cpath2, cpath3, ContactsSearch, DefaultLength1, NoContactMsg1]

#To Field contacts search xpath parts
Topath0="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[1]/div/div[1]/div/div/ul/li/div/span/div/span/div"
Topath1="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[1]/div/div[1]/div/div/ul/li/div/span/div/span/div["
Topath2="]/div/div[2]/div[1]"
Topath3="]/div/div[2]/div[4]"
Topath4="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[1]/div/div[2]/div/h2"
DefaultLength2=1
ToContacts=[Topath0, Topath1, Topath2, Topath3, To, DefaultLength2, Topath4]


#Patient Field contacts search xpath parts
CPFpath0="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[2]/div/div[1]/div/div[2]/span/div/span/div"
CPFpath1="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[2]/div/div[1]/div/div[2]/span/div/span/div["
CPFpath2="]/div/div/div[1]"
CPFpath3="]/div/div/div[3]"
CPFpath4="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[2]/div/div[1]/div/div[2]/span/div/div/div[2]"
CDefaultLength2=1
ComposePFContacts=[CPFpath0, CPFpath1, CPFpath2, CPFpath3, Patient, DefaultLength2, CPFpath4]

#Patient Field contacts search xpath parts
PFpath0="//*[@id='directory-lookup-results']/div"
PFpath1="//*[@id='directory-lookup-results']/div["
PFpath2="]/div/div[2]"
PFpath3="]/div/div[4]"
PFpath4="//*[@id='directory-lookup-results']/div[1]/h2"
DefaultLength2=0
PFContacts=[PFpath0, PFpath1, PFpath2, PFpath3, ContactsSearch, DefaultLength2, NoContactMsg1]

#CONVERSATION SETTINGS SEARCH XPATH PARTS
cspath0="//*[@id='threadSettingsModal']/div[2]/div[4]/div/div/div[1]/div[2]/span/div/span/div"
cspath1="//*[@id='threadSettingsModal']/div[2]/div[4]/div/div/div[1]/div[2]/span/div/span/div["
cspath2="]/div/div[2]/div[1]"
cspath3="]/div/div[2]/div[4]"
cspath4="//*[@id='threadSettingsModal']/div[2]/div[4]/div/div/div[1]/div[2]/span/div/div"
DefaultLength3=1
CSContacts=[cspath0, cspath1, cspath2, cspath3, AddTextBox, DefaultLength3, cspath4]

#Manage Group SEARCH XPATH PARTS
MGpath0="//div[2]/span/div/span/div"
MGpath1="//div[2]/span/div/span/div["
MGpath2="]/div/div[2]/div[1]"
MGpath3="]/div/div[2]/div[4]"
MGpath4="//div[4]/div/div/div[1]/div[2]/span/div/div"
DefaultLength3=1
MGsearch=[MGpath0, MGpath1, MGpath2, MGpath3, AddTextBox, DefaultLength3, MGpath4]

#CoverageSearch Search Parths
Coveragepath0="//*[starts-with(@id, 'coverage-results-')]/div"
Coveragepath1="//*[starts-with(@id, 'coverage-results-')]/div["
Coveragepath2="]/div[2]/div[1]"
Coveragepath3="]/div[2]/div[4]"
Coveragepath4=Coveragepath0
DefaultLength4=1
CoverageSearch=[Coveragepath0, Coveragepath1, Coveragepath2, Coveragepath3, CurrentCoverage, DefaultLength4, Coveragepath4]

#Edit Profile CoverageSearch Search Parths
EditProfileCoverageSearch=[Coveragepath0, Coveragepath1, Coveragepath2, Coveragepath3, EditProfileCurrentCoverage, DefaultLength4, Coveragepath4]

#CoverageSearch Search Parths
Servicepath0="//div/div[1]/div[2]/div/div[2]/ul/li"
Servicepath1="//div/div[1]/div[2]/div/div[2]/ul/li["
Servicepath2="]/div/div[2]/div"
Servicepath3="]/div/div[2]/div"
Servicepath4="//div/div[1]/div[2]/div/div[2]/ul/div/div[1]"
DefaultLength4=1
ServiceSearch=[Servicepath0, Servicepath1, Servicepath2, Servicepath3, ServiceSearchBar, DefaultLength4, Servicepath4]
