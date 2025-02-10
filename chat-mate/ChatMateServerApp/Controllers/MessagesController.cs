using ChatMateServerApp.Dtos;
using ChatMateServerApp.DbServices.Interfaces;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace ChatMateServerApp.Controllers
{
    [ApiController]
    [Route("api/messages")]
    public class MessagesController : ControllerBase
    {
        private readonly IMessageService _messageService;

        public MessagesController(IMessageService messageService)
        {
            _messageService = messageService;
        }

        // POST: api/messages/send
        [HttpPost("send")]
        //[Authorize]
        public IActionResult SendMessage([FromBody] MessageDto messageDto)
        {
            var result = _messageService.SendMessage(messageDto);
            return Ok(result);
        }

        // GET: api/messages/{conversationId}
        [HttpGet("{conversationId}")]
        //[Authorize]
        public IActionResult GetMessages(int conversationId)
        {
            var messages = _messageService.GetMessages(conversationId);
            return Ok(messages);
        }

        /*// POST: api/messages/{conversationId}/media
        [HttpPost("{conversationId}/media")]
        [Authorize]
        public IActionResult SendMedia(int conversationId, IFormFile mediaFile)
        {
            var result = _messageService.SendMedia(conversationId, mediaFile);
            return Ok(result);
        }*/
    }
}
