import { Telegraf } from 'telegraf';
import axios from 'axios';
import 'dotenv/config'; // Direct modern import for dotenv

/**
 * Bayyan AI Telegram Bot
 * System Designer Approach:
 * - Decoupled API interaction
 * - Robust error handling
 * - User-centric response formatting
 */

const bot = new Telegraf(process.env.TELEGRAM_BOT_TOKEN);
const API_URL = process.env.BAYYAN_API_URL || 'http://localhost:8000';

// 1. Initial Greeting
bot.start((ctx) => {
  ctx.replyWithHTML(
    `<b>Welcome to Bayyan AI Bot 📖</b>\n\n` +
    `Ask any question about the Quran, and I will search the verses for you.\n\n` +
    `<i>Example: What does the Quran say about patience?</i>`
  );
});

// 2. Help Command
bot.help((ctx) => {
  ctx.reply('Just send me a message with your question, and I will provide an AI-generated answer backed by Quranic verses.');
});

// 3. Main Query Handler
bot.on('text', async (ctx) => {
  const query = ctx.message.text;
  
  await ctx.sendChatAction('typing');

  try {
    const response = await axios.get(`${API_URL}/search`, {
      params: { q: query }
    });

    const { answer, matches } = response.data;

    await ctx.replyWithHTML(`<b>🤖 Bayyan AI Answer:</b>\n\n${answer}`);

    if (matches?.length > 0) {
      for (const match of matches) {
        const verseText = 
          `<b>📖 Surah ${match.surah} (${match.ayah})</b>\n\n` +
          `<i>${match.arabic}</i>\n\n` +
          `${match.text}`;
        
        await ctx.replyWithHTML(verseText);
      }
    }

  } catch (error) {
    console.error('Error fetching from Bayyan API:', error.message);
    ctx.reply('⚠️ Sorry, I encountered an error. Please ensure the Bayyan AI server is running.');
  }
});

// 4. Launch Bot
bot.launch()
  .then(() => console.log('🚀 Bayyan AI Telegram Bot is running (ESM)...'))
  .catch((err) => console.error('Failed to launch bot:', err));

process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));
