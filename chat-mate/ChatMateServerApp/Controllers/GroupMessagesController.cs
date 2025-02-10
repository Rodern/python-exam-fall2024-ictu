using ChatMateServerApp.Dtos;
using ChatMateServerApp.DbServices.Interfaces;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System;

namespace ChatMateServerApp.Controllers
{
    [ApiController]
    [Route("api/groups/{groupId}/messages")]
    public class GroupMessagesController : ControllerBase
    {
        private readonly IMessageService _messageService;

        public GroupMessagesController(IMessageService messageService)
        {
            _messageService = messageService;
        }

        // POST: api/groups/{groupId}/messages
        [HttpPost]
        [Authorize]
        public IActionResult SendMessage(int groupId, [FromBody] MessageDto messageDto)
        {
            var result = _messageService.SendMessage(messageDto);
            return Ok(result);
        }

        // GET: api/groups/{groupId}/messages
        [HttpGet]
        [Authorize]
        public IActionResult GetMessages(int groupId)
        {
            var messages = _messageService.GetMessages(groupId);
            return Ok(messages);
        }

        /*// POST: api/groups/{groupId}/messages/media
        [HttpPost("media")]
        [Authorize]
        public IActionResult SendMedia(Guid groupId, IFormFile mediaFile)
        {
            var result = _messageService.SendMedia(groupId, mediaFile);
            return Ok(result);
        }*/
    }
}
