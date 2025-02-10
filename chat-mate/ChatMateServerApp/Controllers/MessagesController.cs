using ChatMateServerApp.Dtos;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace ChatMateServerApp.Controllers
{
    [ApiController]
    [Route("api/messages")]
    public class MessagesController : ControllerBase
    {
        // POST: api/messages/send
        [HttpPost("send")]
        [Authorize]
        public IActionResult SendMessage([FromBody] MessageDto messageDto)
        {
            // Send message logic here
            return Ok();
        }

        // GET: api/messages/{conversationId}
        [HttpGet("{conversationId}")]
        [Authorize]
        public IActionResult GetMessages(Guid conversationId)
        {
            // Retrieve messages logic here
            return Ok();
        }

        // POST: api/messages/{conversationId}/media
        [HttpPost("{conversationId}/media")]
        [Authorize]
        public IActionResult SendMedia(Guid conversationId, [FromForm] IFormFile mediaFile)
        {
            // Send media file logic here
            return Ok();
        }
    }
}
