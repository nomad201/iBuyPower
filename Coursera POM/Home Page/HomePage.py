#Welcome Form:
# 1. Work Experience:
WelcomeTitleForm    = "//h1[@class='head']"
JobInput            = "//div[contains(text(),'Ex: Product Manager')]"
JobLevelList        = "//select[@id='current_occupation_level']"
CompanyInput        = "//div[contains(text(),'Ex: Microsoft')]"
CurrentWorkBox      = "//input[@id='trackedEmployerCheckbox']"
# Trong trường hợp thông tin nhập vào không có trong list có sẵn ( ví dụ tiếng Việt), cần thêm 1 nút RETURN để thông tin nhập vào là 1 loại thông tin mới chưa có trong list.
# [1] = Intern/Trainee, [2] = Junior/Entry-level, [3] = Midlevel, [4] = Lead/Manager
# [5] = Senior Manager/ Director, [6] = Executive, [7] = Not Applicable

# 2. Education:
DegreeList          = "//select[@id='educational_attainment']"
#Dai qua viet sau :))
UniversityInput     = "//div[contains(text(),'Ex: New York University')]"
EducationMajorList  = "//select[@id='education_major']"
CurrentStudyBox     = "//input[@id='trackedActiveUniversityCheckbox']"

# 3. Career Goal:
OccupationInput     = "//div[contains(text(),'Ex: Data Scientist')]"
IndustryInput       = "//div[contains(text(),'Ex: Technology')]"


# Lưu ý: Cần chú ý các cột Input, chưa test thử nhưng nếu test nên thử nhập vào ví dụ "data", nó sẽ ra 1 list các job title như "data engineer", "data analysis" để chọn.

# 4. Skip without basic information:
SkipSignUp          = "//button[normalize-space()='Skip']"

# 5. Continues with basic information:
ContinueSignUp      = "//button[normalize-space()='Continue']"

# 6. Main Function:
WelcomeText         = "//h1[contains(text(),'Welcome!')]"
Home                = "//a[contains(text(),'Home')]"
InProgress          = "//a[contains(text(),'In Progress')]"
Completed           = "//a[contains(text(),'Completed')]"
UserFunctionList    = "//span[@class='rc-UserPortrait__full-name body c-ph-username']"
SearchBoxInput      = "//input[@placeholder='What do you want to learn?']"
SearchBoxEnter      = "//button[@class='nostyle search-button']"
ExploreList         = "//span[@class='_r3zeoj']"        
# Need some one find out what can it does?



EnrollforFreeButton = "//div[contains(text(),'Enroll for Free')]"       
# With each course we can find 3 button like this, they are all the same.
# Có sự khác biệt giữa các khóa học cũ và mới, tùy vào đó sẽ phải xem lại Xpath của nút này. Sẽ chỉnh sửa lại sau.







