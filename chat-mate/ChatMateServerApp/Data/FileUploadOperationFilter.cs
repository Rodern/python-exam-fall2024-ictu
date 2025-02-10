using Microsoft.OpenApi.Models;
using Swashbuckle.AspNetCore.SwaggerGen;

namespace ChatMateServerApp.Data
{
    public class FileUploadOperationFilter : IOperationFilter
    {
        public void Apply(OpenApiOperation operation, OperationFilterContext context)
        {
            var fileParams = context.ApiDescription.ParameterDescriptions
                .Where(p => p.ModelMetadata.ModelType == typeof(IFormFile) || p.ModelMetadata.ModelType == typeof(IEnumerable<IFormFile>))
                .ToList();

            if (fileParams.Count == 0)
            {
                return;
            }

            foreach (var param in fileParams)
            {
                var parameter = operation.Parameters.FirstOrDefault(p => p.Name == param.Name);
                if (parameter != null)
                {
                    operation.Parameters.Remove(parameter);
                }
            }

            operation.RequestBody = new OpenApiRequestBody
            {
                Content =
            {
                ["multipart/form-data"] = new OpenApiMediaType
                {
                    Schema = new OpenApiSchema
                    {
                        Type = "object",
                        Properties = new Dictionary<string, OpenApiSchema>
                        {
                            [fileParams[0].Name] = new OpenApiSchema
                            {
                                Type = "string",
                                Format = "binary"
                            }
                        },
                        Required = new HashSet<string> { fileParams[0].Name }
                    }
                }
            }
            };
        }
    }

}

