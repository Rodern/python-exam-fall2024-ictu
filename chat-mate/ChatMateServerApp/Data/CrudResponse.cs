

namespace ChatMateServerApp.Data
{
	public class CrudResponse: Response
	{
        public CrudResponse()
        {
				
        }
        public CrudResponse(bool success, string message)
		{
			Success = success;
			Message = message;
		}
		public CrudResponse(bool success, string message, string reason)
		{
			Success = success;
			Message = message;
			Reason = reason;
		}
		public string Reason { get; set; } = string.Empty;
	}
}
