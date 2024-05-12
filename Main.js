const { Client } = require('whatsapp-web.js');
const qr = require('qrcode-terminal')
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const client = new Client({
  webVersionCache: {
    type: "remote",
    remotePath:
      "https://raw.githubusercontent.com/wppconnect-team/wa-version/main/html/2.2412.54.html",
  },
});

client.on('qr', qr => {
  console.log('qr: ',qr)
});

function generarNuevoQR() {
  client.on('qr', qr => {
      console.log('qr: ',qr)
  });
}
client.on('ready', () => {
    console.log('Client is ready!')
});

client.on('message', async (msg) => {
    console.log('mensaje: ',msg.body);
    rl.question('respuesta: ', (response) => {
      if (response === './Serbot')
      {
        msg.reply(generarNuevoQR);
      }
      else
      {
        client.sendMessage(response)
        msg.reply(response);
      };
      
    });
});

client.initialize();
