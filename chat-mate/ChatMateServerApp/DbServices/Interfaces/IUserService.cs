using ChatMateServerApp.DbModels;
using ChatMateServerApp.Dtos;
using System.Collections.Generic;

namespace ChatMateServerApp.DbServices.Interfaces
{
    public interface IUserService
    {
        Task<User> RegisterUserAsync(UserRegistrationDto userDto);
        Task<User> AuthenticateUserAsync(UserLoginDto loginDto);
        Task<User> GetUserProfileAsync(int userId);
        Task UpdateUserProfileAsync(int userId, UserProfileDto profileDto);
        Task UploadProfilePictureAsync(int userId, string profilePictureUrl);
    }
}
