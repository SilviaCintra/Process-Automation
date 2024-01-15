library(pdftools)
library(tools)

#Parte 1 exclui primeira páginas dos arquivos que estão na parta "Origem" e salva na pasta "sem ágina 1"
# Pasta de origem dos arquivos PDF
pasta_origem <- "C:\\Users\\silvi\\OneDrive\\Documentos\\Programação\\Lâminas\\Origem"

# Pasta de destino para salvar os arquivos sem a primeira página
pasta_destino <- "C:\\Users\\silvi\\OneDrive\\Documentos\\Programação\\Lâminas\\sem Página 1"

# Listar todos os arquivos PDF na pasta de origem
arquivos_pdf <- list.files(pasta_origem, pattern = "*.pdf", full.names = TRUE)

# Iterar sobre cada arquivo PDF
for (file in arquivos_pdf) {
  #utiliza função subset para excluir página, define o arquivo atual, define as página a serem excluidas,
  #utilizando o lenght para definir a ultima página do arquivo
  #Salva em output na pasta destino concatenando com o basename dele
  pdf_subset(file, pages = 2:pdf_length(file), output = paste(pasta_destino, basename(file), sep="\\",  collapse = NULL))
}


#Parte 2 encontra um arquivo na pasta "Origem 2" que tenha o mesmo nome de um arquivo "Sem página 1", junta eles e salva na pasta final
pasta_origem2 <- "C:\\Users\\silvi\\OneDrive\\Documentos\\Programação\\Lâminas\\Origem 2"
arquivos_origem2 <- list.files(pasta_origem2, pattern = "*.pdf", full.names = TRUE)

pasta_semPágina1 <- "C:\\Users\\silvi\\OneDrive\\Documentos\\Programação\\Lâminas\\sem Página 1"
arquivos_semPágina1 <- list.files(pasta_semPágina1, pattern = "*.pdf", full.names = TRUE)

pasta_final <- "C:\\Users\\silvi\\OneDrive\\Documentos\\Programação\\Lâminas\\Final"

for(arquivo in arquivos_origem2){
  arquivo_encontrado <- FALSE
  for(arquivo2 in arquivos_semPágina1){
    # Verifica se o basename do arquivo2 é igual ao basename do arquivo
    if (basename(arquivo2)==basename(arquivo)){
      # Combina os arquivos e salva no diretório final
      pdf_combine(c(arquivo, arquivo2), output = paste(pasta_final, basename(arquivo2), sep="\\", collapse = NULL))
      arquivo_encontrado <- TRUE
    }
  }
    # Se o arquivo não foi encontrado, imprime o basename dele
  if(arquivo_encontrado == FALSE){
    print(basename(arquivo))
  }
}
  

