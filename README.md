# Bulls and Cows

**Bulls and Cows** is a classic code-breaking game where the player tries to guess a secret number chosen by the computer (or another player). The game is usually played with 4-digit numbers, and each digit is unique.  

## How to Play

1. **Secret Number**: One player (or the computer) chooses a secret number with a fixed number of digits, usually 4, with no repeating digits.  
2. **Guessing**: The other player tries to guess the secret number.  
3. **Feedback**: After each guess, the player who knows the secret number provides feedback in terms of:
   - **Cow**: A digit is correct and in the correct position.  
   - **Bull**: A digit is correct but in the wrong position.  

### Example

- Secret Number: `4271`  
- Guess: `1234`  
- Response: `1 Bull, 2 Cows`  
  - Cow: `2` (correct digit in the correct position)  
  - Bulls: `4` and `1` (correct digits but in the wrong positions)  

The objective of the game is to guess the secret number in as few attempts as possible.  

## Notes

- Typically, numbers do not contain repeated digits.  
- You can adjust the number of digits to make the game easier or harder.
