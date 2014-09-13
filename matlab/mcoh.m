function mu = mcoh(A) % = $\mu(A)$ 

M = size(A,2); % number of rows in $A$
An = normc(A); % normalize columns of $A$ to find $A_n$
cloak=eye(M)~=1; % ones everywhere but on the diagonal
mu=max(max(abs(An'*An).*cloak)); % max off-diagonal term of $A^T_n A_n$
%

%!end (6)

