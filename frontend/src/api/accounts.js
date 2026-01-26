import apiClient from './client';

/**
 * Fetch bank account balances
 * @param {Object} params - Query parameters
 * @param {string} params.date - Single date (YYYY-MM-DD)
 * @param {string} params.start_date - Start date for range
 * @param {string} params.end_date - End date for range
 */
export const getAccountBalances = async (params = {}) => {
  const queryParams = new URLSearchParams();
  
  if (params.date) queryParams.append('date', params.date);
  if (params.start_date) queryParams.append('start_date', params.start_date);
  if (params.end_date) queryParams.append('end_date', params.end_date);
  
  const queryString = queryParams.toString();
  const url = `/bank-account-balances${queryString ? `?${queryString}` : ''}`;
  
  return apiClient.get(url);
};

/**
 * Fetch balance summary with analytics
 * @param {Object} params - Query parameters
 */
export const getBalanceSummary = async (params = {}) => {
  const queryParams = new URLSearchParams();
  
  if (params.date) queryParams.append('date', params.date);
  if (params.start_date) queryParams.append('start_date', params.start_date);
  if (params.end_date) queryParams.append('end_date', params.end_date);
  
  const queryString = queryParams.toString();
  const url = `/balance-summary${queryString ? `?${queryString}` : ''}`;
  
  return apiClient.get(url);
};

/**
 * Fetch low balance alerts
 * @param {number} threshold - Alert threshold (0.0-1.0)
 */
export const getAlerts = async (threshold = 0.1) => {
  return apiClient.get(`/alerts?threshold=${threshold}`);
};
