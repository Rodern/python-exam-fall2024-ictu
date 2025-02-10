using ChatMateServerApp.DbModels;
using ChatMateServerApp.DbServices.Interfaces;
using ChatMateServerApp.Dtos;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using ChatMateServerApp.Data;
using System.Collections.ObjectModel;
using Newtonsoft.Json;

namespace ChatMateServerApp.DbServices
{
    public class StatusService : IStatusService
    {
        private readonly ChatMateContext _context;

        public StatusService(ChatMateContext context)
        {
            _context = context;
        }

        public RequestResponse PostStatus(StatusDto statusDto)
        {
            var status = new Status
            {
                Content = statusDto.Content,
                Timestamp = statusDto.Timestamp,
                MediaUrl = statusDto.MediaUrl,
                UserId = statusDto.UserId
            };
            _context.StatusUpdates.Add(status);
            _context.SaveChanges();
            return new RequestResponse { Data = JsonConvert.SerializeObject(status), Success = true };
        }

        public ObservableCollection<Status> GetStatusUpdates(int userId)
        {
            var statuses = _context.StatusUpdates
                .Where(s => s.UserId == userId)
                .ToList();
            return new ObservableCollection<Status>(statuses);
        }

        public RequestResponse DeleteStatus(int statusId)
        {
            var status = _context.StatusUpdates.Find(statusId);
            if (status != null)
            {
                _context.StatusUpdates.Remove(status);
                _context.SaveChanges();
                return new RequestResponse { Success = true };
            }
            return new RequestResponse { Success = false, Message = "Status not found" };
        }
    }
}
