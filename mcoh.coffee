$blab.mcoh = (A) ->
    eye = (u) -> nm.diag(nm.rep([1,u], 1)[0])
    maxAll = (U) -> max(U.reduce((a,b) -> a.concat(b))...)
    An = $blab.normr(A.transpose()).transpose()
    N = A.size()[1]
    cloak = nm.rep([N, N], 1) - eye(N)
    offDiagInProd = abs(An.transjugate().dot(An))*cloak
    maxAll(offDiagInProd)

