import apiClient from './client';

/**
 * Fetch bank transactions
 * @param {string} from_date - Start date (YYYY-MM-DD)
 * @param {string} to_date - End date (YYYY-MM-DD)
 */
export const getTransactions = async (from_date, to_date) => {
  return apiClient.get(`/bank-transactions?from_date=${from_date}&to_date=${to_date}`);
};

/**
 * Fetch enriched transactions with categories
 * @param {Object} params - Query parameters
 */
export const getEnrichedTransactions = async (params) => {
  const queryParams = new URLSearchParams();
  
  queryParams.append('from_date', params.from_date);
  queryParams.append('to_date', params.to_date);
  
  if (params.category) queryParams.append('category', params.category);
  if (params.min_amount !== undefined) queryParams.append('min_amount', params.min_amount);
  if (params.max_amount !== undefined) queryParams.append('max_amount', params.max_amount);
  if (params.is_debit !== undefined) queryParams.append('is_debit', params.is_debit);
  
  return apiClient.get(`/transactions/enriched?${queryParams.toString()}`);
};

/**
 * Fetch transaction trends
 * @param {string} from_date - Start date (YYYY-MM-DD)
 * @param {string} to_date - End date (YYYY-MM-DD)
 */
export const getTransactionTrends = async (from_date, to_date) => {
  return apiClient.get(`/transactions/trends?from_date=${from_date}&to_date=${to_date}`);
};

/**
 * Fetch all transaction categories
 */
export const getCategories = async () => {
  return apiClient.get('/categories');
};
