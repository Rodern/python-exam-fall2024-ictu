using ChatMateServerApp.Dtos;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace ChatMateServerApp.Controllers
{
    [ApiController]
    [Route("api/status")]
    public class StatusController : ControllerBase
    {
        // POST: api/status
        [HttpPost]
        [Authorize]
        public IActionResult PostStatus([FromBody] StatusDto statusDto)
        {
            // Post status logic here
            return Ok();
        }

        // GET: api/status
        [HttpGet]
        [Authorize]
        public IActionResult GetStatusUpdates()
        {
            // Retrieve status updates logic here
            return Ok();
        }

        // DELETE: api/status/{statusId}
        [HttpDelete("{statusId}")]
        [Authorize]
        public IActionResult DeleteStatus(Guid statusId)
        {
            // Delete status logic here
            return Ok();
        }
    }
}
