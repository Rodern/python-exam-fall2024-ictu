using ChatMateServerApp.DbModels;
using ChatMateServerApp.DbServices.Interfaces;
using ChatMateServerApp.Dtos;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using ChatMateServerApp.Data;
using Newtonsoft.Json;
using System.Collections.ObjectModel;
using AutoMapper;

namespace ChatMateServerApp.DbServices
{
    public class UserService : IUserService
    {
        private readonly ChatMateContext _context;
        private readonly IMapper _mapper;

        public UserService(ChatMateContext context, IMapper mapper)
        {
            _context = context;
            _mapper = mapper;
        }

        public RequestResponse RegisterUser(UserRegistrationDto userDto)
        {
            var user = new User
            {
                UserId = 0,
                FirstName = userDto.FirstName,
                LastName = userDto.LastName,
                UserName = userDto.UserName,
                PhoneNumber = userDto.PhoneNumber,
                Groups = null!,
                StatusUpdates = null!,
                ProfilePictureUrl = "https://th.bing.com/th/id/OIP.4Q7-yMnrlnqwR4ORH7c06AHaHa?rs=1&pid=ImgDetMain",
                MessagesReceived = null!,
                MessagesSent = null!,

            };
            _context.Users.Add(user);
            _context.SaveChanges();
            return new RequestResponse { Data = JsonConvert.SerializeObject(user), Success = true };
        }

        public RequestResponse AuthenticateUser(UserLoginDto loginDto)
        {
            var user = _context.Users
                .FirstOrDefault(u => u.UserName == loginDto.UserName && u.PhoneNumber == loginDto.PhoneNumber);
            return new RequestResponse { Data = JsonConvert.SerializeObject(user), Success = user != null };
        }

        public RequestResponse GetUserProfile(int userId)
        {
            var user = _context.Users.Find(userId);
            return new RequestResponse { Data = JsonConvert.SerializeObject(user), Success = user != null };
        }

        public ObservableCollection<UserProfileDto> GetUserProfiles()
        {
            var users = _context.Users;
            return _mapper.Map<ObservableCollection<UserProfileDto>>(users);
        }

        public RequestResponse UpdateUserProfile(int userId, UserProfileDto profileDto)
        {
            var user = _context.Users.Find(userId);
            if (user != null)
            {
                user.FirstName = profileDto.FirstName;
                user.LastName = profileDto.LastName;
                user.UserName = profileDto.UserName;
                user.ProfilePictureUrl = profileDto.ProfilePictureUrl;
                _context.SaveChanges();
                return new RequestResponse { Success = true };
            }
            return new RequestResponse { Success = false, Message = "User not found" };
        }

        public RequestResponse UploadProfilePicture(int userId, string profilePictureUrl)
        {
            var user = _context.Users.Find(userId);
            if (user != null)
            {
                user.ProfilePictureUrl = profilePictureUrl;
                _context.SaveChanges();
                return new RequestResponse { Success = true };
            }
            return new RequestResponse { Success = false, Message = "User not found" };
        }
    }
}
