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
    public class MessageService : IMessageService
    {
        private readonly ChatMateContext _context;

        public MessageService(ChatMateContext context)
        {
            _context = context;
        }

        public RequestResponse SendMessage(MessageDto messageDto)
        {
            var message = new Message
            {
                Content = messageDto.Content,
                Timestamp = messageDto.Timestamp,
                SenderId = messageDto.SenderId,
                ReceiverId = messageDto.ReceiverId,
                GroupId = messageDto.GroupId
            };
            _context.Messages.Add(message);
            _context.SaveChanges();
            return new RequestResponse { Data = JsonConvert.SerializeObject(message), Success = true };
        }

        public ObservableCollection<Message> GetMessages(int conversationId)
        {
            var messages = _context.Messages
                .Where(m => m.ReceiverId == conversationId || m.GroupId == conversationId)
                .ToList();
            return  new ObservableCollection<Message>(messages);
        }

        public RequestResponse SendMedia(int conversationId, string mediaUrl)
        {
            var message = new Message
            {
                Content = mediaUrl,
                Timestamp = DateTime.Now,
                ReceiverId = conversationId
            };
            _context.Messages.Add(message);
            _context.SaveChanges();
            return new RequestResponse { Success = true };
        }
    }
}
