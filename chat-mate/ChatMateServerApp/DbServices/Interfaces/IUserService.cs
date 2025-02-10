using ChatMateServerApp.DbModels;
using ChatMateServerApp.Dtos;
using ChatMateServerApp.Data;
using System.Collections.Generic;
using System.Collections.ObjectModel;

namespace ChatMateServerApp.DbServices.Interfaces
{
    public interface IUserService
    {
        RequestResponse RegisterUser(UserRegistrationDto userDto);
        RequestResponse AuthenticateUser(UserLoginDto loginDto);
        RequestResponse GetUserProfile(int userId);
        RequestResponse UpdateUserProfile(int userId, UserProfileDto profileDto);
        RequestResponse UploadProfilePicture(int userId, string profilePictureUrl);
        ObservableCollection<UserProfileDto> GetUserProfiles();
    }
}
