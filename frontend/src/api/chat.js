import apiClient from './client';

/**
 * Send a chat message to the assistant
 * @param {Object} request - Chat request
 * @param {string} request.message - User message
 * @param {string} request.session_id - Optional session ID
 */
export const sendChatMessage = async (request) => {
  return apiClient.post('/chat', request);
};

/**
 * Get chat history for a session
 * @param {string} session_id - Session identifier
 */
export const getChatHistory = async (session_id) => {
  return apiClient.get(`/chat/history/${session_id}`);
};

/**
 * Delete a chat session
 * @param {string} session_id - Session identifier
 */
export const deleteChatSession = async (session_id) => {
  return apiClient.delete(`/chat/${session_id}`);
};

/**
 * List all active chat sessions
 */
export const listChatSessions = async () => {
  return apiClient.get('/chat/sessions');
};
