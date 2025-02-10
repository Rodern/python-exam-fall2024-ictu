using ChatMateServerAp.Dtos;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace ChatMateServerAp.Controllers
{
    [ApiController]
    [Route("api/groups/{groupId}/messages")]
    public class GroupMessagesController : ControllerBase
    {
        // POST: api/groups/{groupId}/messages
        [HttpPost]
        [Authorize]
        public IActionResult SendMessage(Guid groupId, [FromBody] MessageDto messageDto)
        {
            // Send group message logic here
            return Ok();
        }

        // GET: api/groups/{groupId}/messages
        [HttpGet]
        [Authorize]
        public IActionResult GetMessages(Guid groupId)
        {
            // Retrieve group messages logic here
            return Ok();
        }

        // POST: api/groups/{groupId}/messages/media
        [HttpPost("media")]
        [Authorize]
        public IActionResult SendMedia(Guid groupId, [FromForm] IFormFile mediaFile)
        {
            // Send group media file logic here
            return Ok();
        }
    }
}
