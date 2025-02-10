using ChatMateServerApp.Dtos;
using ChatMateServerApp.DbServices.Interfaces;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace ChatMateServerApp.Controllers
{
    [ApiController]
    [Route("api/users")]
    public class UsersController : ControllerBase
    {
        private readonly IUserService _userService;

        public UsersController(IUserService userService)
        {
            _userService = userService;
        }

        // POST: api/users/register
        [HttpPost("register")]
        public IActionResult Register([FromBody] UserRegistrationDto registrationDto)
        {
            var result = _userService.RegisterUser(registrationDto);
            return Ok(result);
        }

        // POST: api/users/login
        [HttpPost("login")]
        public IActionResult Login([FromBody] UserLoginDto loginDto)
        {
            var token = _userService.AuthenticateUser(loginDto);
            if (token != null)
            {
                return Ok(new { Token = token });
            }
            return Unauthorized();
        }

        // GET: api/users/profile
        [HttpGet("profile")]
        //[Authorize]
        public IActionResult GetProfile(int userId)
        {
            var profile = _userService.GetUserProfile(userId);
            return Ok(profile);
        }

        // GET: api/users/profiles
        [HttpGet("profiles")]
        //[Authorize]
        public IActionResult GetProfiles()
        {
            var profile = _userService.GetUserProfiles();
            return Ok(profile);
        }

        // PUT: api/users/profile
        [HttpPut("profile")]
        //[Authorize]
        public IActionResult UpdateProfile(int userId, [FromBody] UserProfileDto profileDto)
        {
            var result = _userService.UpdateUserProfile(userId, profileDto);
            return Ok(result);
        }

        /*// PUT: api/users/profile-picture
        [HttpPut("profile-picture")]
        [Authorize]
        public IActionResult UploadProfilePicture(IFormFile profilePicture)
        {
            var userId = User.Identity.Name;
            var result = _userService.UploadProfilePicture(userId, profilePicture);
            return Ok(result);
        }*/
    }
}
