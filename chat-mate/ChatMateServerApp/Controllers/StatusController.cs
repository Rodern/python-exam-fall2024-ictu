using ChatMateServerApp.Dtos;
using ChatMateServerApp.DbServices.Interfaces;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System;

namespace ChatMateServerApp.Controllers
{
    [ApiController]
    [Route("api/status")]
    public class StatusController : ControllerBase
    {
        private readonly IStatusService _statusService;

        public StatusController(IStatusService statusService)
        {
            _statusService = statusService;
        }

        // POST: api/status
        [HttpPost]
        //[Authorize]
        public IActionResult PostStatus([FromBody] StatusDto statusDto)
        {
            var result = _statusService.PostStatus(statusDto);
            return Ok(result);
        }

        // GET: api/status
        [HttpGet]
        //[Authorize]
        public IActionResult GetStatusUpdates(int userId)
        {
            var statusUpdates = _statusService.GetStatusUpdates(userId);
            return Ok(statusUpdates);
        }

        // DELETE: api/status/{statusId}
        [HttpDelete("{statusId}")]
        //[Authorize]
        public IActionResult DeleteStatus(int statusId)
        {
            var result = _statusService.DeleteStatus(statusId);
            return Ok(result);
        }
    }
}
