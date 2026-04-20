import { Telegraf } from 'telegraf';
import 'dotenv/config';
import { logger } from './utils/logger.js';
import { startCommand } from './commands/start.js';
import { helpCommand } from './commands/help.js';
import { queryHandler } from './commands/query.js';

/**
 * Bayyan AI Telegram Bot
 * Refactored Architecture for Maintainability
 */

if (!process.env.TELEGRAM_BOT_TOKEN) {
  logger.error('TELEGRAM_BOT_TOKEN is missing in .env');
  process.exit(1);
}

const bot = new Telegraf(process.env.TELEGRAM_BOT_TOKEN);

// Register Commands
bot.start(startCommand);
bot.help(helpCommand);

// Register Main Handler
bot.on('text', queryHandler);

// Launch Bot
bot.launch()
  .then(() => logger.info('Bayyan AI Telegram Bot is running (ESM)...'))
  .catch((err) => logger.error('Failed to launch bot:', err));

// Enable graceful stop
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));
