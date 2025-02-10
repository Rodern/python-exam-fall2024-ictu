using ChatMateServerApp.DbModels;
using ChatMateServerApp.DbServices.Interfaces;
using ChatMateServerApp.Dtos;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace ChatMateServerApp.DbServices
{
    public class UserService : IUserService
    {
    private readonly ChatMateContext _context;

    public UserService(ChatMateContext context)
    {
        _context = context;
    }

    public async Task<User> RegisterUserAsync(UserRegistrationDto userDto)
    {
        var user = new User
        {
            FirstName = userDto.FirstName,
            LastName = userDto.LastName,
            UserName = userDto.UserName,
            PhoneNumber = userDto.PhoneNumber
        };
        _context.Users.Add(user);
        await _context.SaveChangesAsync();
        return user;
    }

    public async Task<User> AuthenticateUserAsync(UserLoginDto loginDto)
    {
        return await _context.Users
            .FirstOrDefaultAsync(u => u.UserName == loginDto.UserName && u.PhoneNumber == loginDto.PhoneNumber);
    }

    public async Task<User> GetUserProfileAsync(int userId)
    {
        return await _context.Users.FindAsync(userId);
    }

    public async Task UpdateUserProfileAsync(int userId, UserProfileDto profileDto)
    {
        var user = await _context.Users.FindAsync(userId);
        if (user != null)
        {
            user.FirstName = profileDto.FirstName;
            user.LastName = profileDto.LastName;
            user.UserName = profileDto.UserName;
            user.ProfilePictureUrl = profileDto.ProfilePictureUrl;
            await _context.SaveChangesAsync();
        }
    }

    public async Task UploadProfilePictureAsync(int userId, string profilePictureUrl)
    {
        var user = await _context.Users.FindAsync(userId);
        if (user != null)
        {

                user.ProfilePictureUrl = profilePictureUrl;
                await _context.SaveChangesAsync();
            }
        }
    }
}
