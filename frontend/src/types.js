/**
 * @typedef {Object} Transaction
 * @property {string} id
 * @property {string} operation_date - ISO date string (YYYY-MM-DD)
 * @property {number} amount
 * @property {boolean} is_debit
 * @property {string} currency
 * @property {{ name: string, color?: string }} [category]
 * @property {string} [merchant]
 * @property {string} [account]
 * @property {string[]} [tags]
 */

/**
 * @typedef {Object} BalanceSummary
 * @property {string} date - ISO date string
 * @property {number} total_balance
 * @property {number} account_count
 * @property {number} average_balance
 * @property {number} highest_balance
 * @property {number} lowest_balance
 * @property {number} total_overdraft_allowed
 * @property {string} currency
 */

/**
 * @typedef {Object} AccountBalance
 * @property {string} account_id
 * @property {string} date - ISO date string
 * @property {number} balance
 * @property {string} currency
 */
