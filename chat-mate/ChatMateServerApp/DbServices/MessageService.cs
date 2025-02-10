using ChatMateServerApp.DbModels;
using ChatMateServerApp.DbServices.Interfaces;
using ChatMateServerApp.Dtos;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace ChatMateServerApp.DbServices
{
    public class MessageService : IMessageService
    {
        private readonly ChatMateContext _context;

        public MessageService(ChatMateContext context)
        {
            _context = context;
        }

        public async Task<Message> SendMessageAsync(MessageDto messageDto)
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
            await _context.SaveChangesAsync();
            return message;
        }

        public async Task<IEnumerable<Message>> GetMessagesAsync(int conversationId)
        {
            return await _context.Messages
                .Where(m => m.ReceiverId == conversationId || m.GroupId == conversationId)
                .ToListAsync();
        }

        public async Task SendMediaAsync(int conversationId, string mediaUrl)
        {
            var message = new Message
            {
                Content = mediaUrl,
                Timestamp = DateTime.Now,
                ReceiverId = conversationId
            };
            _context.Messages.Add(message);
            await _context.SaveChangesAsync();
        }
    }
}
