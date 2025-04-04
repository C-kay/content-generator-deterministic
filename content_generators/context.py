from dataclasses import dataclass
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field

@dataclass
class Content:
    id: Optional[int]
    name: Optional[str] 
    content: Optional[str] 

@dataclass
class WorkflowResponse:
    content: Optional[list[Content]] 