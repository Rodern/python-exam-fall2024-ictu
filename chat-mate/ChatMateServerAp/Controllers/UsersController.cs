using ChatMateServerAp.Dtos;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace ChatMateServerAp.Controllers
{
    [ApiController]
    [Route("api/users")]
    public class UsersController : ControllerBase
    {
        // POST: api/users/register
        [HttpPost("register")]
        public IActionResult Register([FromBody] UserRegistrationDto registrationDto)
        {
            // Registration logic here
            return Ok();
        }

        // POST: api/users/login
        [HttpPost("login")]
        public IActionResult Login([FromBody] UserLoginDto loginDto)
        {
            // Authentication logic here
            return Ok();
        }

        // GET: api/users/profile
        [HttpGet("profile")]
        [Authorize]
        public IActionResult GetProfile()
        {
            // Retrieve user profile logic here
            return Ok();
        }

        // PUT: api/users/profile
        [HttpPut("profile")]
        [Authorize]
        public IActionResult UpdateProfile([FromBody] UserProfileDto profileDto)
        {
            // Update user profile logic here
            return Ok();
        }

        // PUT: api/users/profile-picture
        [HttpPut("profile-picture")]
        [Authorize]
        public IActionResult UploadProfilePicture([FromForm] IFormFile profilePicture)
        {
            // Upload and set profile picture logic here
            return Ok();
        }
    }
}
