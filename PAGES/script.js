alert("Olá, primeiro vamos fazer o cadastro")
let pergunta=prompt("Qual seu nome?")
let pergunta2=prompt("Ok, agora qual o endereço onde você achou a irregularidade?")
alert("perfeito agora escolha em qual das opções abaixo a irregularidade se encaixa?")
let opcoes=prompt("1-Buraco 2-vazamento 3-lixo 4-outro")
if(opcoes=="1"){ 
    let especifique1=prompt("tem mais alguma informação que gostaria de dar?")
    document.write("Muito obrigado pela sua ajuda. Iremos analizar e cuidar do buraco o mais rapido possivel")
}
else if(opcoes=="2"){ 
    let especifique2=prompt("tem mais alguma informação que gostaria de dar?")
    document.write("Muito obrigado pela sua ajuda. Iremos analizar o vazamento e resolver o mais rapido possivel")
}
else if(opcoes=="3"){ 
    let especifique3=prompt("tem mais alguma informação que gostaria de dar?")
    document.write("Muito obrigado pela sua ajuda. Iremos remover o lixo o mais rapido possivel")
}
else{ 
    let especifique4=prompt("tem mais alguma informação que gostaria de dar?")
    document.write("Muito obrigado pela sua ajuda. Iremos analizar o problema e tentar resolvelo o mais rapido possivel")
}