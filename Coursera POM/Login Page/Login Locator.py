#Login 
LoginButton        = "//a[normalize-space()='Log In']"
SignUpButton       = "//span[contains(text(),'Join for Free')]"
FullNameInput      = "//input[@id='name']"
EmailInput         = "//input[@id='email']"
PasswordInput      = "//input[@id='password']"
ShowPasswordButton = "//button[@aria-label='Show password']"
SubmitSignUpButton = "//button[@type='submit']"

# Special Login
GoogleLogin        = "//button[@data-track-component='continue_with_google_auth_btn']"       
# 1 y tuong hay nhung chua setup kip

TempailCopy        = "(//*[name()='path' and contains(@fill-rule,'evenodd')])[2]"



# Bug nhỏ của chức năng Signup ( Phán đoán 10%) , sau khi nhập mật khẩu sai định dạng họ yêu cầu, nhập mật khẩu mới đạt yêu cầu của họ sẽ hiện ra 2 con mắt để xem mật khẩu vừa đặt.
# Lưu ý khi dùng TempMail: Nên bật tạm ẩn danh để lấy 1 tempmail khác trước khi viết cho bài chính thức, nhằm tránh việc web không gen ra tempmail mới để sử dụng.


