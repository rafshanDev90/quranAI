import axios from 'axios';
import { logger } from '../utils/logger.js';

const API_URL = process.env.BAYYAN_API_URL || 'http://localhost:8000';

export const queryHandler = async (ctx) => {
  const query = ctx.message.text;
  
  await ctx.sendChatAction('typing');

  try {
    const response = await axios.get(`${API_URL}/search`, {
      params: { q: query }
    });

    const { answer, matches } = response.data;

    // Added ☪️ icon to the header
    await ctx.replyWithHTML(`<b>☪️ Bayyan AI Answer:</b>\n\n${answer}`);

    if (matches?.length > 0) {
      for (const match of matches) {
        // Added 🕌 icon to the verse header
        const verseText = 
          `<b>🕌 Surah ${match.surah} (${match.ayah})</b>\n\n` +
          `<i>${match.arabic}</i>\n\n` +
          `${match.text}`;
        
        await ctx.replyWithHTML(verseText);
      }
    }

  } catch (error) {
    logger.error('Error fetching from Bayyan API:', error);
    // Added ⚠️ icon for errors
    ctx.reply('⚠️ Sorry, I encountered an error. Please ensure the Bayyan AI server is running.');
  }
};
