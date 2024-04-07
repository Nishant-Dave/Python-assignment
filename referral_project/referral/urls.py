from django.urls import path
from referral.api.views import UserRegistration, UserDetails, ReferralsList, MyTokenObtainPairView, MyTokenRefreshView

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('details/', UserDetails.as_view(), name='details'),
    path('referrals/', ReferralsList.as_view(), name='referrals'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),

]

