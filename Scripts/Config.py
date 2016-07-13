CureatrPlayURL="https://cureatr-vm.dev:5101/"
#CureatrPlayURL="https://messenger.play.cureatr.com/"

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
#ManageGroups="div.check-label.link.js-manage-groups"
SelectMGContact="//div[2]/span/div/span/div[1]/div/div[2]/div[1]"
CreateGroupLink="//*[@id='createGroupLink']"
SelectExistingGroup="//div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]"
GroupNameInput="//*[@id='groupNameInput']"
CreateGroup="//*[@id='createGroup']"
AddRecipientInGroup="//div[9]/div/div/div/div"
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
#ShowMoreLinks="//div[1]/div[5]/div/div/a"
NoContactMsg1="//*[@id='directory-lookup-results']/div[1]/h2"
NoContactMsg2="//*[@id='directory-lookup-results']/div[1]/div"
showmoremessages="//div[1]/div[5]/div/div/a"

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
QuickMsgSaveBtn2="(//a[contains(text(),'Save')])[2]"
QuickMsgHeader="div.modal-header.clearfix > div.modal-title.truncate-text"
QuickMsgDialogClose="div.modal-close.cancel"
QuickMsgListNum="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[2]/div/div/div[2]/ul/li[10]/div[1]/div"
ReplyQMListNum="//*[@id='main-content']/div/div[2]/div/div[2]/div/div[3]/div/div/div[2]/ul/li[8]/div[1]/div"
QMDelete="//div/div[1]/div/div[2]/ul[2]/li[1]/div[2]/a"
QMUpdate="//ul[2]/li/div[3]/form/textarea"

#New Message
NewMsgTitle="//*[@id='content']/div[3]/div/div/div[2]/div/div/div[1]"
NewMsgClose="div.modal-close.js-modal-close"
NewMsgMinimize="//*[@id='content']/div[3]/div/div/div[2]/div/div/div[2]/div[1]"
ToLabel="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[1]/div/div[1]/label"
PatientLabel="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[2]/div/div[1]/label"
WorkflowLabel="//*[@id='workflow-select-view']/div[1]/label"
SubjectLabel="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[5]/label"
#PressEnterToSend="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[3]/div[2]/label/span"
PressEnterToSend="//div/div[1]/div[3]/div[2]/label/span"
To="//*[@id='new-thread-to']"
SelectRecipient="//span/div[1]/div/div[2]/div"
SelectedRecipient="//fieldset/div[1]/div/div[1]/div/div/ul/li[1]/div[1]"
#Patient="//*[@id='new-thread-patient']"
Patient="//*[@id='new-thread-patient-no-pcm']"
Workflow="//*[@id='new-thread-workflow']"
ClickRecipientInTo="//fieldset/div/div/div/div/div/ul/li/div"
RemoveRecipientInTo="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[1]/div/div[1]/div/div/ul/li[1]/a"
Subject="//*[@id='new-thread-subject']"
MsgBody="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[2]/div[1]/textarea"
SendBtn="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[2]/div[2]/div[1]/div"
SendBtn1="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[2]/div[2]"
SendBtnCss="div.send-button-text"
#MsgBodyPart="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[2]/div[1]/div[2]/div[2]/div[2]"
MsgBodyPart="//li[2]/div[1]/div[2]/div[2]/div[2]"
SubjectPart="//*[@id='main-content']/div/div[1]/div/div[2]/div"
#FileInputButton="//div[@id='fileinput-button']/input"
FileInputButton="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[3]/div[1]/div/div/input"
FileInputButtonTwo="//*[@id='main-content']/div/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/input"
UrgentMessage="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[1]/div[2]/div/label"
UrgentMessage2="//*[@id='main-content']/div/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/label"
FileUploadInput="//*[@id='fileinput-button']/input"
FileUpload="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[3]/div[1]/div/div/label[1]"
QuikckMsgBtn="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[2]/div[2]/div[2]"
QuickMsgHelpText="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[2]/div/div/div[3]/div[2]"
QuickMsgCancelBtn="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[2]/div/div/div[3]/div[3]/a"
EditListBtn="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[2]/div/div/div[3]/div[1]/a"
ComposeScreenSize="//*[@id='content']/div[3]/div/div/div[2]/div"
AttachmentLink="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[3]/div[1]/div/div/label[2]"
AttachmentLink2="//html/body/div[1]/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[3]/div[1]/div/div/input"
EditQM="//div/div[1]/div/div[2]/ul[2]/li[1]/div[2]/div[2]/span"
QMPopUpCloseBtn="a.link-secondary.cancel"
ImageText="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[2]/div[1]/div[2]/div[2]/div[2]/ul[2]"
UploadedImg="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[2]/div[1]/div[2]/div[2]/div[2]/ul[1]/div/div[1]/div/img"
UploadedImg1="//div/div[1]/div/img"
UrgentToastOne="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[1]/div[1]"
UrgentToast="//*[@id='main-content']/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]"

#FileInputButton2="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[3]/div[1]/div/div/label[2]"

#To Field Contact Details
ContactName="//div/span/div/span/div/div/div[2]/div[1]"
ContactSpecialty="//div/span/div/span/div/div/div[2]/div[2]"
ContactTitle="//div/span/div/span/div/div/div[2]/div[4]"
ContactStatus="//div/span/div/span/div/div/div[2]/div[1]/div/img"
ThreadProfileImg="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[2]/div[1]/div[1]/img"
#Cancel New Conversation Pop UP
ConverMsg="//div/div[1]/div[1]/div[1]"
DiscardMsg="//div/div[1]/div[2]/p"
ConverCancelBtn="//div/div[1]/div[3]/div[1]/a"
ConverDiscardBtn="//div/div[1]/div[3]/div[2]/a"


PatientName="//*[@id='main-content']/div/div[1]/div/div[2]/div"
ConversationWith="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[1]/div/div/div"
ReadRecipt="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[2]/div[2]/div/span"
SentMsg="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[2]/div[2]/div/div"
ReplyReadRecipt="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[3]/div[2]/div/span"
SentTime="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[2]/div[2]/div/div"
MsgBodyPartTextArea="//*[@id='main-content']/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/textarea"
QuickMsgIcon2="//*[@id='main-content']/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]"

NotificationIcon="//*[@id='eventsDropdown']/div/div[1]"

#CHAT THREAD
ChatThread="//*[@id='thread-collection']/li[1]/div[2]/div[2]/div[1]/div[1]"
ReplyMsgBody="//*[@id='main-content']/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/textarea"
LatestMsgBodyPart="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[3]/div[1]/div[2]/div[2]/div[2]"
LatestMsgBodyPart1="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[4]/div[1]/div[2]/div[2]/div[2]"
#OffDutyMsgBodyPart="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[4]/div[1]/div[2]/div[2]/div[2]"
ReplySendBtn="//*[@id='main-content']/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[1]/div"
ReplySendBtn2="//div[2]/div/div/div[2]/div[3]/div[2]"
ThreadCount="//*[@id='thread-collection']/li/div[2]/div[1]/div[1]/div"
UrgentMsgFlag="//*[@id='thread-collection']/li/div[2]/div[2]/div[2]/div[1]/div"
UrgentMsgIconSent="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[2]/div[1]/div[2]/div[2]/div[1]"
UrgentMsgIconReply="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[3]/div[1]/div[2]/div[2]/div[1]"

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
EditProfileStatus="//div[3]/form/div[1]/div/div[2]/div[2]"
EditProfileStatusBusy="//*[starts-with(@id, 'toggle-status-menu-')]/div[3]/label[2]"


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
#cpath0="//*[@id='main-search']/div[2]"
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

#CoverageSearch Search Parts
Coveragepath0="//*[starts-with(@id, 'coverage-results-')]/div"
Coveragepath1="//*[starts-with(@id, 'coverage-results-')]/div["
Coveragepath2="]/div[2]/div[1]"
Coveragepath3="]/div[2]/div[4]"
Coveragepath4=Coveragepath0
DefaultLength4=1
CoverageSearch=[Coveragepath0, Coveragepath1, Coveragepath2, Coveragepath3, CurrentCoverage, DefaultLength4, Coveragepath4]

#Edit Profile CoverageSearch Search Parts
EditProfileCoverageSearch=[Coveragepath0, Coveragepath1, Coveragepath2, Coveragepath3, EditProfileCurrentCoverage, DefaultLength4, Coveragepath4]

#CoverageSearch Search Parts
Servicepath0="//div/div[1]/div[2]/div/div[2]/ul/li"
Servicepath1="//div/div[1]/div[2]/div/div[2]/ul/li["
Servicepath2="]/div/div[2]/div"
Servicepath3="]/div/div[2]/div"
Servicepath4="//div/div[1]/div[2]/div/div[2]/ul/div/div[1]"
DefaultLength4=1
ServiceSearch=[Servicepath0, Servicepath1, Servicepath2, Servicepath3, ServiceSearchBar, DefaultLength4, Servicepath4]


QuickMessage0="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[2]/div/div/div[2]/ul/li/div"
QuickMessage1="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[2]/div/div/div[2]/ul/li["
QuickMessage2="]/div[2]/div"
MsgListNum=[QuickMessage0, QuickMessage1, QuickMessage2]

DelQuickMessage0="//div/div[1]/div/div[2]/ul[2]/li"
DelQuickMessage1="//div/div[1]/div/div[2]/ul[2]/li["
DelQuickMessage2="]/div[2]/a"
DelQuickMessage3=ConverDiscardBtn
DeleteQuikMsgList=[DelQuickMessage0, DelQuickMessage1, DelQuickMessage2, DelQuickMessage3]

UploadCancelButton0="//div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[4]/div/div/div"
UploadCancelButton1="//div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[4]/div/div/div["
UploadCancelButton2="]/div/div/div[3]/button"
UploadCancelButton=[UploadCancelButton0,UploadCancelButton1,UploadCancelButton2]

UploadSuccessIcon0="//div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[4]/div/div/div"
UploadSuccessIcon1="//div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[4]/div/div/div["
UploadSuccessIcon2="]/div/div/div[1]/div"
UploadSuccessIcon=[UploadSuccessIcon0,UploadSuccessIcon1,UploadSuccessIcon2]

UploadCancelIcon0="//div[1]/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[4]/div/div/div"
UploadCancelIcon1="//div[1]/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[4]/div/div/div["
UploadCancelIcon2="]/div/div/div[2]/div"
UploadCancelIcon=[UploadCancelIcon0,UploadCancelIcon1,UploadCancelIcon2]

UploadCancelButtonTwo0="//div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div"
UploadCancelButtonTwo1="//div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div["
UploadCancelButtonTwo2="]/div/div/div[3]/button"
UploadCancelButtonTwo=[UploadCancelButtonTwo0,UploadCancelButtonTwo1,UploadCancelButtonTwo2]

UploadSuccessIconTwo0="//div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div"
UploadSuccessIconTwo1="//div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div["
UploadSuccessIconTwo2="]/div/div/div[1]/div"
UploadSuccessIconTwo=[UploadSuccessIconTwo0,UploadSuccessIconTwo1,UploadSuccessIconTwo2]

UploadCancelIconTwo0="//div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div"
UploadCancelIconTwo1="//div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div["
UploadCancelIconTwo2="]/div/div/div[2]/div"
UploadCancelIconTwo=[UploadCancelIconTwo0,UploadCancelIconTwo1,UploadCancelIconTwo2]

LatestMsg0="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li"
LatestMsg1="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li["
LatestMsg2="]/div[1]/div[2]/div[2]/div[2]"
LatestMsg=[LatestMsg0,LatestMsg1,LatestMsg2]

LatestImage0="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li"
LatestImage1="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li["
LatestImage2="]/div[1]/div[2]/div[2]/div[2]"
LatestImage3="]/div[1]/div[2]/div[2]/div[2]/ul[1]/div/div[1]/div/img"
LatestImage=[LatestImage0,LatestImage1,LatestImage2,LatestImage3]

LatestFile0="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li"
LatestFile1="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li["
LatestFile2="]/div[1]/div[2]/div[2]/div[2]"
LatestFile3="]/div[1]/div[2]/div[2]/div[2]/ul[2]/li/div/figure/img"
LatestFile=[LatestFile0,LatestFile1,LatestFile2,LatestFile3]

LatestMp3File0="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li"
LatestMp3File1="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li["
LatestMp3File2="]/div[1]/div[2]/div[2]/div[2]"
LatestMp3File3="]/div[1]/div[2]/div[2]/div[2]/ul[2]/li/div/div/a/span"
LatestMp3File=[LatestMp3File0,LatestMp3File1,LatestMp3File2,LatestMp3File3]

ReadRecipt0="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li"
ReadRecipt1="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li["
ReadRecipt2="]/div[2]/div/span"
ReadRecipt3="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li["
ReadRecipt4="]/div[1]/div[2]/div[2]/div[2]"
ReadReciptTwo=[ReadRecipt0,ReadRecipt1,ReadRecipt2, ReadRecipt3, ReadRecipt4]

#CONVERSATION SETTINGS
ConversationSettings="//*[@id='main-content']/div/div[1]/div/div[1]/div"
unarchivelabel="//*[@id='thread-collection']/li[1]/div[2]/div[2]/div[1]/div[1]"
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
ReplyThread="//*[@id='thread-collection']/li[1]/div[2]"
SaveText="//*[@id='threadSettingsModal']/div[2]/div[1]/div[1]/div[2]"
ListOfUsers="//*[@id='threadSettingsModal']/div[2]/div[2]"
CSHeader="//*[@id='threadSettingsModal']/div[1]/div[1]"
FirstRecipient="//*[@id='threadSettingsModal']/div[2]/div[2]/div[1]"
CloseBtnCss="div.close"
CreateButton="//*[@id='threadSettingsModal']/div[2]/div[1]/div[2]/div/button"
RemoveLink="//*[@id='threadSettingsModal']/div[2]/div[2]/div[1]/div[2]/div[5]/a"
ClickOnUser="//*[@id='threadSettingsModal']/div[2]/div[4]/div/div/div[1]/div[2]/span/div/span/div[1]/div"
GMClose="//div/div/div/div[1]/div[2]/div/div[4]/div/div/div[1]/div[3]"
AddedThread="//div/div/div/div[1]/div[1]/div[1]"
Sendmsgconversations1="//div[4]/div/a"
Closebtnconversations1="//*[@id='56778fc85b3f054b396cf83e']/div[1]/button"
cancellabel="html/body/div[7]/div/div[1]/div[3]/div[1]/a"
CancelLeaveText="html/body/div[9]/div/div[1]/div[3]/div[1]/a"
LatestThread="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[3]/div/div/div"
LeaveText="//*[@id='main-content']/div/div[2]/div/div[2]/div/div[2]"
ImgProfile="//div[3]/div[1]/img"
AddRecipientList="//*[@id='threadSettingsModal']/div[2]/div[4]/div/div/div[2]"
RemovedVerifyText="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[5]/div/div/div"
ArchieveText="//*[@id='bottomCheckboxActions']/div/div[1]/label/div"
MuteText="//*[@id='bottomCheckboxActions']/div/div[2]/label/div"
MuteIcon="//*[@id='thread-collection']/li[2]/div[2]/div[2]/div[3]"
MuteIcon1="//*[@id='thread-collection']/li[1]/div[2]/div[2]/div[3]"
SelectToPerson="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[1]/div/div[1]/div/div/ul/li/div/span/div/span/div[3]/div"
ReplyLeaveText="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[6]/div/div/div"
#To="//*[@id='new-thread-to']"
#SelectedRecipient="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[1]/div/div[1]/div/div/ul/li/div/span/div/span/div[3]/div"
#MsgBody="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[2]/div[1]/textarea"
#SendBtn="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[7]/div/div[1]/div[2]/div[2]/div[1]/div"
Services="//div[3]/div[4]/div/ul/li"
CloseServices="//*[@id='role-users-modal']/div[1]/div[2]/div"
#MessagesList="//div[3]/div[5]/div/div/ul/li[1]/div[2]/div[2]/div[1]/div[1]"
MessagesList="//div[3]/div[5]/div/div/ul/li/div[2]/div[1]/div[2]/img"
Status="//div[3]/div[1]/div/div[3]/span"
Name="//*[@id='56778fc85b3f054b396cf83e']/div[3]/div[1]/div/div[2]"
Speciality="//div[3]/div[2]/div[3]/div[2]"
Title="//div[3]/div[2]/div[3]/div[1]"
SHeader="//*[@id='role-users-modal']/div[1]/div[1]"
SendLinkText="//*[@id='role-users-modal']/div[3]/a"
EditIcon="//*[@id='role-users-modal']/div[2]/div/div/div[1]/div[2]/div[5]"
ListUser="//*[@id='role-users-modal']/div[2]/div/div/div[1]"
SendUser="//*[@id='content']/div[3]/div/div/div[2]/div/form/fieldset/div[1]/div/div[1]/div/div/ul/li[1]/div[1]"
CloseTo="//*[@id='content']/div[3]/div/div/div[2]/div/div/div[2]/div[2]"
MessageDisplayed="//*[@id='main-content']/div/div[2]/div/div[1]/div/ul/li[2]/div[1]/div[2]/div[2]/div[2]"
#MessagesList="//div[3]/div[5]/div/div/div"
ConverMsg="//div/div[1]/div[1]/div[1]"
DiscardMsg="//div/div[1]/div[2]/p"
ConverCancelBtn="html/body/div[7]/div/div[1]/div[3]/div[1]/a"
ConverDiscardBtn="//div/div[1]/div[3]/div[2]/a"
CloseIcon="//div/div[1]/div[1]/div[2]/div"
Closepatientwindow1="//*[@id='content']/div[3]/div/div/div[2]/div/div/div[2]/div[2]"
popupcloseicon="html/body/div[7]/div/div[1]/div[1]/div[2]/div"
Recipient="//*[@id='threadSettingsModal']/div[2]/div[2]/div"