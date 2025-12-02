"""
Peer Matching Algorithm
Matches users based on stress profile similarity
"""

from typing import List, Tuple
from app.models import UserProfile

def calculate_match_score(user1: UserProfile, user2: UserProfile) -> int:
    """
    Calculate how similar two users are
    Returns score 0-100 (100 = perfect match)
    """
    
    score = 0
    
    # Same profession = +30 points
    if user1.profession == user2.profession:
        score += 30
    
    # Same salary range = +25 points
    if user1.salary_range == user2.salary_range:
        score += 25
    
    # Same main stress = +30 points
    if user1.main_stress == user2.main_stress:
        score += 30
    
    # Similar mood (within 2 points) = +15 points
    if abs(user1.mood_average - user2.mood_average) <= 2:
        score += 15
    
    return score

def find_best_match(current_user: UserProfile, all_users: List[UserProfile]) -> Tuple[UserProfile, int]:
    """
    Find the best matching peer for a user
    
    Args:
        current_user: The user looking for a match
        all_users: All available users in system
    
    Returns:
        (best_matched_user, match_score)
    """
    
    best_match = None
    best_score = 0
    
    # Compare with each user
    for user in all_users:
        # Don't match with self
        if user.user_id == current_user.user_id:
            continue
        
        # Calculate score
        score = calculate_match_score(current_user, user)
        
        # Keep track of best match
        if score > best_score:
            best_score = score
            best_match = user
    
    return best_match, best_score

def find_top_matches(current_user: UserProfile, all_users: List[UserProfile], top_n: int = 5) -> List[Tuple[UserProfile, int]]:
    """
    Find top N matching peers (sorted by score)
    """
    
    matches = []
    
    for user in all_users:
        if user.user_id == current_user.user_id:
            continue
        
        score = calculate_match_score(current_user, user)
        matches.append((user, score))
    
    # Sort by score (highest first)
    matches.sort(key=lambda x: x, reverse=True)
    
    # Return top N
    return matches[:top_n]

