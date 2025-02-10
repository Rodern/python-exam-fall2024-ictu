using ChatMateServerApp.DbModels;
using ChatMateServerApp.DbServices.Interfaces;
using ChatMateServerApp.Dtos;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace ChatMateServerApp.DbServices
{
    public class StatusService : IStatusService
    {
        private readonly ChatMateContext _context;

        public StatusService(ChatMateContext context)
        {
            _context = context;
        }

        public async Task<Status> PostStatusAsync(StatusDto statusDto)
        {
            var status = new Status
            {
                Content = statusDto.Content,
                Timestamp = statusDto.Timestamp,
                MediaUrl = statusDto.MediaUrl,
                UserId = statusDto.UserId
            };
            _context.StatusUpdates.Add(status);
            await _context.SaveChangesAsync();
            return status;
        }

        public async Task<IEnumerable<Status>> GetStatusUpdatesAsync(int userId)
        {
            return await _context.StatusUpdates
                .Where(s => s.UserId == userId)
                .ToListAsync();
        }

        public async Task DeleteStatusAsync(int statusId)
        {
            var status = await _context.StatusUpdates.FindAsync(statusId);
            if (status != null)
            {
                _context.StatusUpdates.Remove(status);
                await _context.SaveChangesAsync();
            }
        }
    }
}
